package com.alex.dudchenko.sts.repo;

import com.alex.dudchenko.sts.model.User;
import org.springframework.data.repository.CrudRepository;

public interface UserRepository extends CrudRepository<User, Long> {

    User findByUsername(String username);
}
