package com.arlekinside.miroservices.scheduler.controllers;

import com.arlekinside.miroservices.scheduler.exceptions.NotFoundException;
import com.arlekinside.miroservices.scheduler.models.ApplicationException;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;

@ControllerAdvice
@Slf4j
public class ExceptionHandlerControllerAdvice {

    @ExceptionHandler({NotFoundException.class})
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ResponseEntity<ApplicationException> handleNotFound(NotFoundException ex) {
        log.info("Not found exception message={}", ex.getMessage());

        var response = ApplicationException.builder()
                .exceptionType(ex.getClass().getSimpleName())
                .message(ex.getMessage())
                .build();

        return ResponseEntity
                .status(HttpStatus.NOT_FOUND)
                .body(response);
    }

    @ExceptionHandler({Throwable.class})
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ResponseEntity<ApplicationException> handleUnexpected(Throwable ex) {
        log.error("Server error", ex);

        var response = ApplicationException.builder()
                .message("Server error")
                .exceptionType("Server error")
                .build();

        return ResponseEntity
                .internalServerError()
                .body(response);
    }
}
