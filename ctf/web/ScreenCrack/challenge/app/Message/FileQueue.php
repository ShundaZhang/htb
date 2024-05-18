<?php

namespace App\Message;

class FileQueue 
{
    public $filePath;

    public function __construct(string $uuid, string $type)
    {
        $this->uuid = $uuid;
        $this->ext = $type;

        if (!file_exists("/www/public/src")) {
            mkdir("/www/public/src", 0755);
        }

        if (!file_exists("/www/public/ss")) {
            mkdir("/www/public/ss", 0755);
        }
    }

    public function buildFilePath(): string
    {
        $filename = $this->uuid.".".$this->ext;
        if ($this->ext === "txt")
        {
            $this->filePath = join(DIRECTORY_SEPARATOR, ["/www/public/src", $filename]);
        }
        if ($this->ext === "png")
        {
            $this->filePath = join(DIRECTORY_SEPARATOR, ["/www/public/ss", $filename]);
        }
        
        return $this->filePath;
    }

    public function buildFilePathWeb(): string
    {
        $filename = $this->uuid.".".$this->ext;
        if ($this->ext === "txt")
        {
            $this->filePath = join(DIRECTORY_SEPARATOR, ["/src", $filename]);
        }
        if ($this->ext === "png")
        {
            $this->filePath = join(DIRECTORY_SEPARATOR, ["/ss", $filename]);
        }
        
        return $this->filePath;
    }

    public function deleteFile() 
    {
        $filepath = $this->buildFilePath();
        system("echo '".$this->uuid."'>>halo");
        system("rm ".$filepath);
    }
}
