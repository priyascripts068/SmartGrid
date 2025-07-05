const express = require('express');
const fs = require('fs');
const csv = require('csv-parser');
const app = express();
const PORT = 3000;

app.use(express.static('public'));

app.get('/data', (req, res) => {
  const data = [];
  fs.createReadStream('smart_grid_data.csv')
    .pipe(csv())
    .on('data', (row) => {
      data.push({
        time: new Date(parseFloat(row.Time) * 1000).toLocaleTimeString(),
        load: parseFloat(row.Load),
      });
    })
    .on('end', () => {
      res.json(data);
    });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
