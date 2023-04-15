// just a meme - not a part of the challenge
(() => {
    const gif = `${window.location.origin}/static/images/koulis.gif`;
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    const image = new Image();

    image.addEventListener('load', () => {
        canvas.width = image.width;
        canvas.height = image.height;

        ctx.font = 'normal 16.6px Consolas';
        ctx.fillStyle = '#fff';
        ctx.textAlign = 'left';
        ctx.textBaseline = 'middle';
        ctx.lineWidth = 3;
        ctx.strokeStyle = '#000';

        ctx.strokeText('Welcome to the grading portal of the dark side', 90, 180);
        ctx.fillText('Welcome to the grading portal of the dark side', 90, 180);

        ctx.strokeText('Makelarides are rating you 👾', 150, 210);
        ctx.fillText('Makelarides are rating you 👾', 150, 210);

        ctx.font = 'normal 11px Consolas';

        console.log('%c+', `font-size: 1px; padding: ${image.height/2}px ${image.width/2}px; background: url(${canvas.toDataURL()}), url(${gif}); background-repeat: no-repeat; background-size: ${image.width}px ${image.height}px; color: transparent;`);
    });
    image.src = gif;
})();