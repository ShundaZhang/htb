<?php
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpFoundation\Request;

class DefaultController extends AbstractController
{
    public function index(Request $request): Response
    {
        $location = $request->get('location');

        if (empty($location))
        {
            $latitude = mt_rand(-90, 90) + mt_rand() / mt_getrandmax();
            $longitude = mt_rand(-180, 180) + mt_rand() / mt_getrandmax();
            $location = "($latitude, $longitude)";
        } 
        
        $message = $this->container->get('twig')->createTemplate(
                "Located at: {$location} from your ship's computer"
            )
            ->render();
 
        return $this->render('base.html.twig', [
            'message' => $message ?? ''
        ]);
    }
}