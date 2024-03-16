<?php

namespace App\Controllers;

use CodeIgniter\Controller;
use CodeIgniter\API\ResponseTrait;
use Firebase\JWT\JWT;
use Firebase\JWT\Key;

class UserController extends Controller
{
    use ResponseTrait;

    public function LoginIndex()
    {
        return View("LoginPage");
    }
    public function login()
    {
        $db = db_connect();
        $json_data = request()->getJSON(true);
        if (!count($json_data) == 2) {
            return $this->respond("Please provide username and password", 404);
        }
        $query = $db->table("users")->getWhere($json_data, 1, 0);
        $result = $query->getRowArray();
        if (!$result) {
            return $this->respond("User not found", 404);
        } else {
            $key = (string) getenv("JWT_SECRET");
            $iat = time();
            $exp = $iat + 36000;
            $headers = [
                "alg" => "HS256",
                "typ" => "JWT",
            ];
            $payload = [
                "iat" => $iat,
                "exp" => $exp,
                "username" => $result["username"],
            ];
            $token = JWT::encode($payload, $key, "HS256");

            $response = [
                "message" => "Login Succesful",
                "token" => $token,
            ];
            return $this->respond($response, 200);
        }
    }

    public function RegisterIndex()
    {
        return View("RegisterPage");
    }
    public function register()
    {
        $db = db_connect();
        $json_data = request()->getJSON(true);
        $username = $json_data["username"] ?? null;
        $password = $json_data["password"] ?? null;

        if (!($username && $password)) {
            return $this->respond("Empty username or password", 404);
        } else {
            // Check if the username already exists
            $existingUser = $db
                ->table("users")
                ->where("username", $username)
                ->get()
                ->getRow();

            if ($existingUser) {
                return $this->respond("Username already exists", 400);
            }

            // Insert the new user if the username is unique
            $db->table("users")->insert([
                "username" => $username,
                "password" => $password,
            ]);

            if ($db->affectedRows() > 0) {
                return $this->respond(
                    "Registration successful for user: " . $username,
                    200
                );
            } else {
                return $this->respond("Registration failed", 404);
            }
        }
    }
}
