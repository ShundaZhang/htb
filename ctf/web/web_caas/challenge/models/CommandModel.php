<?php
class CommandModel
{
    public function __construct($url)
    {
        $this->command = "curl --proto =http,https -sSL " . escapeshellcmd($url) . " 2>&1";
    }

    public function exec()
    {
        $output = shell_exec($this->command);
        return $output;
    }
}