const prompt = require('prompt-sync')({ sigint: true })

console.log(
  'En enklare konverterare \nProgrammet skall ersätta alla siffror skrivna med text till siffror.'
)

const dict = {
  ett: 1,
  två: 2,
  tre: 3,
  fyra: 4,
  fem: 5,
  sex: 6,
  sju: 7,
  åtta: 8,
  nio: 9,
  tio: 10,
}

let text = 'q'

while (text === 'q') {
  text = prompt('Mata in en mening med små bokstäver (Avsluta med q).')
  for (const key in dict) {
    if (text.includes(key)) {
      text.replace(key, dict[key])
    }
  }
  console.log('Den konverterade texten blev som följer: ')
  console.log(text)
}
