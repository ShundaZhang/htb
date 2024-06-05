<?php

namespace App\Http\Controllers;

use App\Services\SiteShotService;
use Illuminate\Http\Request;

class SiteShotController extends Controller
{
    public function getHtml(Request $request)
    {
        $site = $request->input('site');
	#print($site)

        if (!$this->validateurl($site)) {
            return  response()->json([
                'status' => 'failed',
                'message' => 'Dont do naughty stuff.'
            ]);
        }

        if (!isset($site)) {
            return response()->json([
                'status' => 'failed',
                'message' => 'Need site parameter'
            ]);
        }

        $ssSrv = new SiteShotService();

        return $ssSrv->getHtmlResp($site);
    }

    public function getSS(Request $request)
    {

        $site = $request->input('site');

        if (!$this->validateUrl($site)) {
            return  response()->json([
                'status' => 'failed',
                'message' => 'Dont do naughty stuff.'
            ]);
        }

        if (!isset($site)) {
            return response()->json([
                'status' => 'failed',
                'message' => 'Need site parameter'
            ]);
        }
        
        if (!(substr($site, 0, strlen("http://")) === "http://" || substr($site, 0, strlen("https://")) === "https://")) {
            $site = "http://".$site;
        }

        $ssSrv = new SiteShotService();

        return $ssSrv->getScreenShotResp($site);
    }
    
    private function isValidIPv4($ip) {
        return filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4) !== false;
    }

    private function isValidDomain($domain) {
        $pattern = '/^(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9])$/i';
        if (!preg_match($pattern, $domain)) {
            return false;
        }
    
        if (!checkdnsrr($domain, 'A') && !checkdnsrr($domain, 'AAAA')) {
            return false;
        }
    
        return true;
    }

    private function isLocalIP($ip) {
        if (!filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE)) {
            return true;
        }

        if (!filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_RES_RANGE)) {
            return true;
        }

        return false;
    }

    private function validateUrl($url) {
        $parsedUrl = parse_url($url);

        if (!isset($parsedUrl['host'])) {
            return false;
        }

        if ($this->isValidIPv4($parsedUrl['host']) && $this->isLocalIP($parsedUrl['host'])) {
            return false;
        }

        if (!$this->isValidDomain($parsedUrl['host'])) {
            return false;
        }

        return true;
    }
}

