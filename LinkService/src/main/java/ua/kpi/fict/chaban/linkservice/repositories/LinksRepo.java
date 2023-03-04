package ua.kpi.fict.chaban.linkservice.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ua.kpi.fict.chaban.linkservice.entities.Link;

import java.util.List;

@Repository
public interface LinksRepo extends JpaRepository<Link, Long> {
    Link findLinkByCode(String code);

    List<Link> findLinksByUserId(Long userId);
}

