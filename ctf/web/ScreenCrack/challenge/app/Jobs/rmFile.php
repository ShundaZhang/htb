<?php

namespace App\Jobs;

use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldBeUnique;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Queue\SerializesModels;

use App\Message\FileQueue;

class rmFile implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public $fileQueue;
    /**
     * Create a new job instance.
     */
    public function __construct(FileQueue $fileQueue)
    {
        $this->fileQueue = $fileQueue;
    }

    /**
     * Execute the job.
     */
    public function handle(): void
    {
        $this->fileQueue->deleteFile();
    }
}
