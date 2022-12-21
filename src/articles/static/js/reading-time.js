document.addEventListener('DOMContentLoaded', () => 
{
    function readingTime(text) 
    {
        const wpm = 225;
        const words = text.trim().split(/\s+/).length;
        const time = Math.ceil(words / wpm);
    
        return time
    }
    
    const text = document.querySelector('#article').innerText
    document.querySelector("#reading-time").innerText = readingTime(text);
})
