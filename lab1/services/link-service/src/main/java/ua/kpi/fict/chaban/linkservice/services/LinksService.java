package ua.kpi.fict.chaban.linkservice.services;

import org.springframework.stereotype.Service;
import ua.kpi.fict.chaban.linkservice.entities.Link;

import javax.naming.NameAlreadyBoundException;

@Service
public interface LinksService {
    public Link createLink(Link link) throws NameAlreadyBoundException;

    public Iterable<Link> getUserLinks(Long userId);

    public Long deleteLink(Long linkId);

    public Link updateLink(Link link, String newShortLink) throws NameAlreadyBoundException;

    public Link updateLinkById(Long linkId, String newShortLink) throws NameAlreadyBoundException;
}
