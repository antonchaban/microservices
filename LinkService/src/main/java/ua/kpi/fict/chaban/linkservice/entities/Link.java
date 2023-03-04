package ua.kpi.fict.chaban.linkservice.entities;

import jakarta.persistence.*;
import lombok.*;

import java.time.Instant;
import java.util.Date;

@Entity
@Table(name = "links")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode
@ToString
public class Link {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column(name = "code")
    private String code;

    @Column(name = "url")
    private String url;

    @Column(name = "user_id")
    private Long userId;

    @Column(name = "expires_stamp")
    private Instant expiresStamp;

    @Column(name = "created_stamp")
    private Instant createdStamp;
}
