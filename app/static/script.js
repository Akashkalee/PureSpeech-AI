document.addEventListener('DOMContentLoaded', () => {
    const textInput = document.getElementById('text-input');
    const voiceSelect = document.getElementById('voice-select');
    const rateInput = document.getElementById('rate-input');
    const pitchInput = document.getElementById('pitch-input');
    const rateValue = document.getElementById('rate-value');
    const pitchValue = document.getElementById('pitch-value');
    const speakBtn = document.getElementById('speak-btn');
    const stopBtn = document.getElementById('stop-btn');
    const visualizerBars = document.querySelectorAll('.visualizer-bar');
    const pauseBtns = document.querySelectorAll('.btn-pause');

    // Pause Insertion Logic
    pauseBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const duration = btn.getAttribute('data-duration');
            const pauseTag = ` [pause ${duration}] `;

            // Insert at cursor position
            const startPos = textInput.selectionStart;
            const endPos = textInput.selectionEnd;
            const text = textInput.value;

            textInput.value = text.substring(0, startPos) + pauseTag + text.substring(endPos);

            // Restore cursor position after the tag
            textInput.selectionStart = textInput.selectionEnd = startPos + pauseTag.length;
            textInput.focus();
        });
    });

    let audio = null;

    // Fetch Voices
    async function loadVoices() {
        try {
            const response = await fetch('/api/voices');
            const voices = await response.json();

            voiceSelect.innerHTML = '';
            voices.forEach(voice => {
                const option = document.createElement('option');
                option.value = voice.ShortName;
                option.textContent = `${voice.FriendlyName} (${voice.Gender})`;
                voiceSelect.appendChild(option);
            });
        } catch (error) {
            console.error('Error loading voices:', error);
            voiceSelect.innerHTML = '<option disabled>Error loading voices</option>';
        }
    }

    loadVoices();

    // Update Sliders
    rateInput.addEventListener('input', (e) => {
        const val = e.target.value;
        rateValue.textContent = `${val >= 0 ? '+' : ''}${val}%`;
    });

    pitchInput.addEventListener('input', (e) => {
        const val = e.target.value;
        pitchValue.textContent = `${val >= 0 ? '+' : ''}${val}Hz`;
    });

    // Speak
    speakBtn.addEventListener('click', async () => {
        const text = textInput.value.trim();
        if (!text) return;

        setLoading(true);

        try {
            const response = await fetch('/api/synthesize', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    text: text,
                    voice: voiceSelect.value,
                    rate: `${rateInput.value >= 0 ? '+' : ''}${rateInput.value}%`,
                    pitch: `${pitchInput.value >= 0 ? '+' : ''}${pitchInput.value}Hz`
                })
            });

            if (!response.ok) throw new Error('Synthesis failed');

            const blob = await response.blob();
            const url = URL.createObjectURL(blob);

            // Setup Download Button
            const downloadBtn = document.getElementById('download-btn');
            downloadBtn.href = url;
            downloadBtn.style.display = 'flex';
            downloadBtn.download = `speech-${new Date().getTime()}.mp3`;

            if (audio) {
                audio.pause();
                URL.revokeObjectURL(audio.src);
            }

            audio = new Audio(url);
            audio.onplay = () => setPlaying(true);
            audio.onended = () => setPlaying(false);
            audio.play();

        } catch (error) {
            console.error('Error synthesizing:', error);
            alert('Failed to synthesize speech. Please try again.');
            setLoading(false);
        }
    });

    // Stop
    stopBtn.addEventListener('click', () => {
        if (audio) {
            audio.pause();
            audio.currentTime = 0;
            setPlaying(false);
        }
    });

    function setLoading(isLoading) {
        speakBtn.disabled = isLoading;
        speakBtn.innerHTML = isLoading ? '<span class="icon">⌛</span> Generating...' : '<span class="icon">▶</span> Speak';
    }

    function setPlaying(isPlaying) {
        speakBtn.disabled = isPlaying;
        stopBtn.disabled = !isPlaying;

        visualizerBars.forEach(bar => {
            if (isPlaying) {
                bar.classList.add('animating');
            } else {
                bar.classList.remove('animating');
            }
        });
    }
    // Word and Char Count
    const charCountEl = document.getElementById('char-count');
    const wordCountEl = document.getElementById('word-count');

    function updateStats() {
        const text = textInput.value;
        const charCount = text.length;
        const wordCount = text.trim() === '' ? 0 : text.trim().split(/\s+/).length;

        charCountEl.textContent = `${charCount} characters`;
        wordCountEl.textContent = `${wordCount} words`;
    }

    textInput.addEventListener('input', updateStats);

    // Initial call
    updateStats();

});
