<?php

use App\Controllers\ProfileController;
use CodeIgniter\Router\RouteCollection;
use App\Controllers\UserController;
/**
 * @var RouteCollection $routes
 */
$routes->get('/', 'Home::index');
$routes->get('/login',[UserController::class,'LoginIndex']);
$routes->post('/login',[UserController::class,'login']);
$routes->get('/register',[UserController::class,'RegisterIndex']);
$routes->post('/register',[UserController::class,'register']);
$routes->get('/profile',[ProfileController::class,'index'],['filter' => 'authenticated' ]);

