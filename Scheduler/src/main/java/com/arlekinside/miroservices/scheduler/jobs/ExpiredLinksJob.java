package com.arlekinside.miroservices.scheduler.jobs;

import com.arlekinside.miroservices.scheduler.services.LinkService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
@Slf4j
public class ExpiredLinksJob {

    private final LinkService linkService;

    public ExpiredLinksJob(LinkService linkService) {
        this.linkService = linkService;
    }

    @Scheduled(cron = "${shortener.scheduler.job.expired.link.cron}")
    public void cleanExpiredLinks() {
        log.info("Running expired links cron job");
        linkService.deleteExpired();
        log.info("Expired links cron job complete");
    }
}
