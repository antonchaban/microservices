package com.arlekinside.miroservices.scheduler.exceptions;

public class LinkNotFoundException extends NotFoundException {

    public LinkNotFoundException(int id) {
        super(createMessage(id));
    }

    private static String createMessage(int id) {
        return String.format("Link with id=%d not found", id);
    }
}
