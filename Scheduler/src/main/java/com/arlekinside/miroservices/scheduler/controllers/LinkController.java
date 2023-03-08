package com.arlekinside.miroservices.scheduler.controllers;

import com.arlekinside.miroservices.scheduler.exceptions.NotFoundException;
import com.arlekinside.miroservices.scheduler.models.Link;
import com.arlekinside.miroservices.scheduler.services.LinkService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/scheduler")
public class LinkController {

    private final LinkService linkService;

    public LinkController(LinkService linkService) {
        this.linkService = linkService;
    }

    @GetMapping("link/{id}/renew")
    public Link renewLicense(@PathVariable("id") int id) throws NotFoundException {
        return linkService.renewLicense(id);
    }
}
