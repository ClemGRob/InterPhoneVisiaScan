import QtQuick 2.12
import QtQuick.Controls 2.15
import "Constants.js" as Constants

ApplicationWindow {
    visible: true
    title : Constants.textenameprojet
    width: Constants.fullscreenWidth
    height: Constants.fullscreenHeight
    color: Constants.colorgris

    flags: Qt.FramelessWindowHint | Qt.Window

    Rectangle {
        id: rectanglerotation
        x: 0
        y: 0
        width: Constants.fullscreenWidth
        height: Constants.fullscreenHeight
        rotation : Constants.sensrotationApp
        color: Constants.transparent
        UnderApp {}
    }
}