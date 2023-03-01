package com.arlekinside.miroservices.scheduler.services.impl;

import com.arlekinside.miroservices.scheduler.exceptions.LinkNotFoundException;
import com.arlekinside.miroservices.scheduler.exceptions.NotFoundException;
import com.arlekinside.miroservices.scheduler.models.Link;
import com.arlekinside.miroservices.scheduler.repositories.LinkRepository;
import com.arlekinside.miroservices.scheduler.services.LinkService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

import java.time.Duration;
import java.time.Instant;

@Service
@Slf4j
public class LinkServiceImpl implements LinkService {
    private final LinkRepository linkRepository;

    @Value("${shortener.links.renewal.days}")
    private long renewalDays;
    public LinkServiceImpl(LinkRepository linkRepository) {
        this.linkRepository = linkRepository;
    }

    @Override
    @Transactional(propagation = Propagation.REQUIRES_NEW, rollbackFor = {Throwable.class})
    public void deleteExpired() {
        var expiredLinks = linkRepository.findAllExpired();

        if (expiredLinks.isEmpty()) {
            log.info("No expired links found. Skipping...");
            return;
        }

        log.info("{} expired links found. Deleting...", expiredLinks.size());

        expiredLinks.forEach(link -> {
            var id = link.getId();
            log.info("Deleting link with id={}, code={}, userId={}", id, link.getCode(), link.getUser().getId());
            linkRepository.delete(link);
            log.info("Link with id={} was deleted successfully", id);
        });
    }

    @Override
    @Transactional(propagation = Propagation.REQUIRES_NEW, rollbackFor = Throwable.class)
    public Link renewLicense(int id) throws NotFoundException {
        log.info("Finding license with id={} for renewal", id);

        var license = linkRepository.findById(id)
                .orElseThrow(() -> new LinkNotFoundException(id));

        log.info("License with id={} found", id);

        var newExpiresStamp = Instant.now().plus(Duration.ofDays(renewalDays));
        license.setExpiresStamp(newExpiresStamp);

        log.info("Saving license with id={} with updated expirationStamp={}", id, license.getExpiresStamp().toString());
        return linkRepository.save(license);
    }
}
