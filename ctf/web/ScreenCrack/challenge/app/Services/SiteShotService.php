<?php

namespace App\Services;

use Ramsey\Uuid\Uuid;
use App\Jobs\rmFile;
use App\Message\FileQueue;

use Illuminate\Support\Facades\Queue;

class SiteShotService
{
    public function getHtmlResp($url) 
    {
        // Create a new cURL resource
        $ch = curl_init();

        // Set cURL options
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_TIMEOUT, 3);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

        // Execute cURL request
        $response = curl_exec($ch);

        // Check for errors
        if (curl_errno($ch)) {
            $error = curl_error($ch);
            curl_close($ch);
            return response()->json([
                'status' => 'failed',
            ]);

        }

        // Get HTTP response code
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

        // Close cURL resource
        curl_close($ch);

        $uuidStr = Uuid::uuid4()->toString();
        $filequeue = new FileQueue($uuidStr, "txt");
        $filenameLocal = $filequeue->buildFilePath();
        $filenameResp = $filequeue->buildFilePathWeb();

        $rf = new rmFile($filequeue);
        Queue::push($rf);

        file_put_contents($filenameLocal, $response);

        return response()->json([
            'status' => 'success',
            'filename' => $filenameResp,
        ]);
    }

    public function getScreenShotResp($url) 
    {
        $ssurl = "https://api.screenshotmachine.com/?key=6b76b2&dimension=1024x768&url=".$url;

        try {
            $filecontents = file_get_contents($ssurl);

            $uuidStr = uuid::uuid4()->tostring();
            $filequeue = new filequeue($uuidStr, "png");
            $filenameLocal = $filequeue->buildfilepath();
            $filenameResp = $filequeue->buildfilepathweb();

            $rf = new rmFile($filequeue);
            Queue::push($rf);

            file_put_contents($filenameLocal, $filecontents);

            return response()->json([
                'status' => 'success',
                'site' => $url,
                'image' => $filenameResp,
            ]);
        } catch (exception $e) {
            return response()->json([
                'status' => 'failed',
            ]);
        }
    }
}
