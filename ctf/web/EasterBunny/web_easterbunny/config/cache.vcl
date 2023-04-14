vcl 4.1;

backend default {
    .host = "127.0.0.1";
    .port = "1337";
}

sub vcl_hash {
    hash_data(req.url);

    if (req.http.host) {
        hash_data(req.http.host);
    } else {
        hash_data(server.ip);
    }

    return (lookup);
}

sub vcl_recv {
    set req.http.X-Forwarded-URL = req.url;
    set req.http.X-Forwarded-Proto = "http";
    if( req.http.host ~ ":[0-9]+" )
    {
        set req.http.X-Forwarded-Port = regsub(req.http.host, ".*:", "");
    }
    else
    {
        set req.http.X-Forwarded-Port = "80";
    }

    if ( !( req.url ~ "^/message") ) {
        unset req.http.Cookie;
    }
}

sub vcl_backend_response {
    if (bereq.url ~ "^/$" || bereq.url ~ "^/letters") {
        set beresp.ttl = 60s;
    } else if (bereq.url ~ "^/message") {
        if(beresp.status != 200)
        {
            set beresp.ttl = 5s;
        }
        else
        {
            set beresp.ttl = 120s;
        }
    } else if (bereq.url ~ "^/static") {
        set beresp.ttl = 120s;
    }
}

sub vcl_deliver {
    if (obj.hits > 0) {
        set resp.http.X-Cache = "HIT";
    } else {
        set resp.http.X-Cache = "MISS";
    }

    set resp.http.X-Cache-Hits = obj.hits;
}
