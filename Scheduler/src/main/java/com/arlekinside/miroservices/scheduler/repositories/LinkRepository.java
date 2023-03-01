package com.arlekinside.miroservices.scheduler.repositories;

import com.arlekinside.miroservices.scheduler.models.Link;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface LinkRepository extends JpaRepository<Link, Integer> {

    @Query("select l from Link l where l.expiresStamp <= current_timestamp")
    List<Link> findAllExpired();
}
