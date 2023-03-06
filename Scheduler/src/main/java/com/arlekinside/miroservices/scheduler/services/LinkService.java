package com.arlekinside.miroservices.scheduler.services;

import com.arlekinside.miroservices.scheduler.exceptions.NotFoundException;
import com.arlekinside.miroservices.scheduler.models.Link;

public interface LinkService {

    void deleteExpired();

    Link renewLicense(int id) throws NotFoundException;
}
