const { app, BrowserWindow, Menu, MenuItem} = require('electron/main')
const path = require('node:path')

const createWindow = () => {
    const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
    })

  win.loadFile('index.html')
  return(win)
}


app.whenReady().then(() => {
  createWindow()
  globalShortcut.register('CommandOrControl+Y', () => { console.log("yay!")})

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})
