<?php
class PageModel
{
    public $file;

    public function __destruct() 
    {
        include($this->file);
    }
}