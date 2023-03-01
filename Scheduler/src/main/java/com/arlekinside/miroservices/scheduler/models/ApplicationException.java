package com.arlekinside.miroservices.scheduler.models;

import lombok.*;

import java.time.ZonedDateTime;

@Builder
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class ApplicationException {

    private final ZonedDateTime timestamp = ZonedDateTime.now();
    private String exceptionType;
    private String message;
}
