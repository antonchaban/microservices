package ua.kpi.fict.chaban.linkservice.controllers;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import net.minidev.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ua.kpi.fict.chaban.linkservice.entities.Link;
import ua.kpi.fict.chaban.linkservice.services.LinksServiceImpl;

import javax.naming.NameAlreadyBoundException;
import java.time.Instant;
import java.time.temporal.ChronoUnit;

@RestController
@RequestMapping("/api/link")
public class LinksController {
    @Autowired
    private LinksServiceImpl linksService;

    @PostMapping("links") // Tested
    public ResponseEntity createLink(@RequestBody JSONObject jsonReq) throws NameAlreadyBoundException, JsonProcessingException { // todo add get user id from session
        var link = new Link();
        link.setUrl(jsonReq.getAsString("url"));
        link.setUserId(Long.parseLong(jsonReq.getAsString("userId")));
        link.setExpiresStamp(jsonReq.get("permanent").equals(true) ? null : Instant.now().plus(30, ChronoUnit.DAYS));
        link.setCode(jsonReq.getAsString("code") != null ? jsonReq.getAsString("code") : linksService.generateRandomString(6));
        return ResponseEntity.ok(linksService.createLink(link));
    }

    @GetMapping("links") // Tested
    public ResponseEntity getUserLinks(@RequestParam("userId") long userId) {
        return ResponseEntity.ok(linksService.getUserLinks(userId));
    }


    @DeleteMapping("links/{linkId}") // Tested
    public ResponseEntity deleteLink(@PathVariable Long linkId) {
        return ResponseEntity.ok("Link with id " + linksService.deleteLink(linkId) + " was deleted");
    }

    @PutMapping("links/{linkId}") // Tested
    public ResponseEntity updateLinkById(@PathVariable Long linkId, @RequestBody JSONObject newShortLink) throws NameAlreadyBoundException {
        return ResponseEntity.ok(linksService.updateLinkById(linkId, newShortLink.getAsString("newShortLink")));
    }

    @GetMapping("links/{code}")
    public ResponseEntity getLinkByCode(@PathVariable String code) {
        return ResponseEntity.status(301).header("Location", linksService.getLinkByCode(code)).build();
    }

}
