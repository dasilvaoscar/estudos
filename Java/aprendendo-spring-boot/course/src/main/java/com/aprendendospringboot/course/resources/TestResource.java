package com.aprendendospringboot.course.resources;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.aprendendospringboot.course.entities.Test;

@RestController
@RequestMapping(value = "/test")
public class TestResource {
	
	@GetMapping
	public ResponseEntity<Test> findAll(){
		Test g = new Test(1L, "Administradores");
		return ResponseEntity.ok().body(g);
	}
}
