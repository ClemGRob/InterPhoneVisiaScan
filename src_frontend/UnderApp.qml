import QtQuick 2.12
import QtQuick.Controls 2.15
import "Constants.js" as Constants

Image {
    id: imageFond_total
    x: 0
    y: 0
    width: Constants.fullscreenWidth
    height: Constants.fullscreenHeight
    source: Constants.picture_fondTotal
    anchors.horizontalCenter: parent.horizontalCenter

    Image {
        id: imageSousFond_V2
        x: 0
        y: 0
        width: Constants.fullscreenWidth
        height: Constants.fullscreenHeight
        source: Constants.picture_SousFond_V2

        Image {
            id: image
            x: Constants.fullscreenWidth * 0.71
            y: Constants.fullscreenHeight * 0.8
            width: Constants.fullscreenWidth * 0.45
            height: Constants.fullscreenHeight * 0.1
            rotation : Constants.rotation
            source: Constants.picture_Ynov_Logo
            fillMode: Image.PreserveAspectFit
        }

// Au besoin de fermer l'UI, décommanté ce code
/* 
        Image {
            id: comptour_P_Logo_GVD
            x: Constants.fullscreenWidth * - 0.01
            y: Constants.fullscreenHeight * - 0.03
            width: Constants.fullscreenWidth * 0.4
            height: Constants.fullscreenHeight * 0.37
            rotation : Constants.rotation
            source: "Images/Comptour_P_Logo_GvD.png"
            rotation: 90
            fillMode: Image.PreserveAspectFit
            Image {
                id: poweron
                x: Constants.fullscreenWidth * 0.12
                y: Constants.fullscreenHeight * 0.09
                width: Constants.fullscreenWidth * 0.15
                height: Constants.fullscreenHeight * 0.15
                rotation: 270
                source: "Images/power-on.png"
                fillMode: Image.PreserveAspectFit
                MouseArea {
                                    anchors.fill: parent
                                    onPressed: parent.color =  Constants.colorbleufoncé // Couleur plus foncée lors de l'appui
                                    onReleased: parent.color = Constants.colorbleu // Retour à la couleur standard lors du relâchement
                }
            }
        }
*/
        Image {
            id: image1
            x: Constants.fullscreenWidth * - 0.01
            y: Constants.fullscreenHeight * - 0.03
            width: Constants.fullscreenWidth * 0.4
            height: Constants.fullscreenHeight * 0.37
            rotation : Constants.rotation
            source: Constants.picture_Comptour_P_Logo_GvD
            fillMode: Image.PreserveAspectFit
            
            Image {
                id: image2
                x: Constants.fullscreenWidth * 0.12
                y: Constants.fullscreenHeight * 0.09
                width: Constants.fullscreenWidth * 0.15
                height: Constants.fullscreenHeight * 0.15
                source: Constants.picture_Temp_Left_Pressed
                fillMode: Image.PreserveAspectFit
                MouseArea {
                    anchors.fill: parent
                        onClicked: {
                            backend.handleButtonPress("Button clicked Previous")
                        }
                    }
                }
            }
        }

        Image {
            id: image3
            x: Constants.fullscreenWidth * - 0.019
            y: Constants.fullscreenHeight * 0.65
            width: Constants.fullscreenWidth * 0.4
            height: Constants.fullscreenHeight * 0.37
            rotation : Constants.rotation
            source: Constants.picture_Comptour_P_Logo_DvG
            fillMode: Image.PreserveAspectFit

            Image {
                id: image4
                x: Constants.fullscreenWidth * 0.12
                y: Constants.fullscreenHeight * 0.09
                width: Constants.fullscreenWidth * 0.15
                height: Constants.fullscreenHeight * 0.15
                source: Constants.picture_Temp_Right_Pressed
                fillMode: Image.PreserveAspectFit
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        backend.handleButtonPress("Button clicked next")
                    }
                }
            }
        }

        Rectangle {
            id: rectangleUnderDefilement
            x: Constants.fullscreenWidth * 0.35
            y: Constants.fullscreenHeight * 0.10
            width: Constants.fullscreenWidth * 0.5
            height: Constants.fullscreenHeight * 0.8
            rotation : Constants.rotation
            color: Constants.colorbleu  
            UnderSwipeMenu {}
        }

        Rectangle {
            id: rectangle2
            x: Constants.fullscreenWidth * 0.19
            y: Constants.fullscreenHeight * 0.45
            width: Constants.fullscreenWidth * 0.2
            height: Constants.fullscreenHeight * 0.15
            radius: 45
            rotation : Constants.rotation
            color: Constants.colorbleu

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    //progressBar.visible = true 
                    //timelineAnimation.running = true 
                    backend.handleButtonPress("Reconnaissance_IA")
                }
                onPressed: parent.color =  Constants.colorbleufoncé 
                onReleased: parent.color = Constants.colorbleu 
            }

            Text {
                id : lbcustom
                anchors.centerIn: parent
                text: "Please start the recognition"
                font.pixelSize: 15
                color: "white"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                /*onTextChanged: {
                    if (text === "Process ending") {
                        backend.handleButtonPress("end Reconnaissance_IA");
                    }
                }*/
            }
        }/*
        ProgressBar {
            id: progressBar
            x: 245
            y: 450
            width: 310
            height: 80
            visible: false
            value: 0
        }
        
        Timeline {
            id: timeline
            animations: [
                TimelineAnimation {
                    id: timelineAnimation
                    running: false
                    loops: 1
                    duration: 3000
                    to: 3000
                    from: 0
                }
            ]
            startFrame: 0
            enabled: true
            endFrame: 3000

            KeyframeGroup {
                target: progressBar
                property: "value"
                Keyframe {
                    frame: 0
                    value: 0
                }

                Keyframe {
                    frame: 3000
                    value: 1
                }
            }
            KeyframeGroup {
                target: progressBar
                property: "scale"
                Keyframe {
                    frame: 2999
                    value: 1
                }

                Keyframe {
                    frame: 3000
                    value: 0
                }
            }
            KeyframeGroup {
                target: lbcustom
                property: "text"
                Keyframe {
                    value: "Start process"
                    frame: 0
                }
                Keyframe {
                    value: "Stop moving, Pichure in 3"
                    frame: 500
                }
                Keyframe {
                    value: "Pichure in 2..."
                    frame: 600
                }
                Keyframe {
                    value: "Pichure in 1..."
                    frame: 700
                }
                Keyframe {
                    value: "Pichure OK..."
                    frame: 900
                }
                Keyframe {
                    value: "Processing, wait ."
                    frame: 1200
                }
                Keyframe {
                    value: "Processing, wait .."
                    frame: 1500
                }
                Keyframe {
                    value: "Processing, wait ..."
                    frame: 1800
                }
                Keyframe {
                    value: "Processing, wait ."
                    frame: 2100
                }
                Keyframe {
                    value: "Processing, wait .."
                    frame: 2400
                }
                Keyframe {
                    value: "Processing, wait ..."
                    frame: 2700
                }
                Keyframe {
                    value: "Process ending"
                    frame: 2999
                } 
                Keyframe {
                    value: "Please start the recognition"
                    frame: 3000
                } 
            }
        }*/
    }
