package ua.kpi.fict.chaban.linkservice.controllers;

import net.minidev.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ua.kpi.fict.chaban.linkservice.entities.Link;
import ua.kpi.fict.chaban.linkservice.services.LinksServiceImpl;

import javax.naming.NameAlreadyBoundException;

@RestController
@RequestMapping("/api/")
public class LinksController {
    @Autowired
    private LinksServiceImpl linksService;

    @PostMapping("links") // Tested
    public ResponseEntity createLink(@RequestBody Link link) throws NameAlreadyBoundException { // todo add get user id from session
        return ResponseEntity.ok(linksService.createLink(link));
    }

    @GetMapping("links") // Tested
    public ResponseEntity getUserLinks(@RequestBody JSONObject userId) {
        Long id = Long.parseLong(userId.getAsString("userId"));
        return ResponseEntity.ok(linksService.getUserLinks(id));
    }


    @DeleteMapping("links/{linkId}") // Tested
    public ResponseEntity deleteLink(@PathVariable Long linkId) {
        return ResponseEntity.ok("Link with id " + linksService.deleteLink(linkId) + " was deleted");
    }

    @PutMapping("links/{linkId}") // Tested
    public ResponseEntity updateLinkById(@PathVariable Long linkId, @RequestBody JSONObject newShortLink) throws NameAlreadyBoundException {
        return ResponseEntity.ok(linksService.updateLinkById(linkId, newShortLink.getAsString("newShortLink")));
    }


}
