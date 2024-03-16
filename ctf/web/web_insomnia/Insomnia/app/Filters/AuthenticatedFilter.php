<?php

namespace App\Filters;

use CodeIgniter\Filters\FilterInterface;
use CodeIgniter\HTTP\RequestInterface;
use CodeIgniter\HTTP\ResponseInterface;
use \Firebase\JWT\JWT;
use Firebase\JWT\Key;
use Config\Services;


class AuthenticatedFilter implements FilterInterface
{
    /**
     * Do whatever processing this filter needs to do.
     * By default it should not return anything during
     * normal execution. However, when an abnormal state
     * is found, it should return an instance of
     * CodeIgniter\HTTP\Response. If it does, script
     * execution will end and that Response will be
     * sent back to the client, allowing for error pages,
     * redirects, etc.
     *
     * @param RequestInterface $request
     * @param array|null       $arguments
     *
     * @return RequestInterface|ResponseInterface|string|void
     */
    public function before(RequestInterface $request, $arguments = null)
    {
        $key = getenv('JWT_SECRET');
        $token = $_COOKIE['token'] ?? null;
    
        if (is_null($token)) {
            $view = Services::renderer()->setData([
                'content' => "I can't see the JWT token :("
            ])->render('ErrorPage');
            
            return Services::response()->setBody($view)->setStatusCode(403);
        }
    
        try{
            JWT::decode($token,new Key($key,'HS256'));
        }catch(\Exception $ex){
            $view = Services::renderer()->setData([
                'content' => "Your JWT token is broken!!!"
            ])->render('ErrorPage');
            
            return Services::response()->setBody($view)->setStatusCode(403);
        }
    
        // If no exceptions occurred, the token is valid
        return null;
    }
    

    /**
     * Allows After filters to inspect and modify the response
     * object as needed. This method does not allow any way
     * to stop execution of other after filters, short of
     * throwing an Exception or Error.
     *
     * @param RequestInterface  $request
     * @param ResponseInterface $response
     * @param array|null        $arguments
     *
     * @return ResponseInterface|void
     */
    public function after(RequestInterface $request, ResponseInterface $response, $arguments = null)
    {
        //
    }
}
