import mainScene from "./scenes/mainScene.js"

const config = {
    type: Phaser.AUTO,
    width: 1920,
    height: 1080,
    parent: 'game',
    physics: {
        default: 'arcade',
        gravity: {y: 300}, 
        debug: true
    } ,
    scene: [mainScene]
}

new Phaser.Game(config)
    