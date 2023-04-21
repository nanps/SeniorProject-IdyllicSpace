const APP_ID = 'd176f6cd28f04644afa6d6093551c6d4'
const TOKEN = sessionStorage.getItem('token')
const CHANNEL = sessionStorage.getItem('room')
let UID = sessionStorage.getItem('UID')
let NAME = sessionStorage.getItem('name')

const client = AgoraRTC.createClient({mode:'rtc', codec:'vp8'})

let localTracks = []
let remoteUsers = {}

let joinAndDisplayLocalStream = async () => {
    client.on('user-published', handleUserJoined)
    client.on('user-left', handleUserLeft)

    try{
        UID = await client.join(APP_ID, CHANNEL, TOKEN, UID)
    }catch(error){
        console.error(error)
    }

    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()
    // localTracks[1].setMuted(true)

    let member = await createMember()

    await client.publish(localTracks)
}

let handleUserJoined = async (user, mediaType) => {
    remoteUsers[user.uid] = user
    await client.subscribe(user, mediaType)

    // if (mediaType === 'video'){
    //     let player = document.getElementById(`user-container-${user.uid}`)
    //     if (player != null){
    //         player.remove()
    //     }

    //     let member = await getMember(user)

    //     player = `<div  class="video-container" id="user-container-${user.uid}">
    //         <div class="video-player" id="user-${user.uid}"></div>
    //         <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
    //     </div>`

    //     document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)
    //     user.videoTrack.play(`user-${user.uid}`)
    // }

    if (mediaType === 'audio'){
        user.audioTrack.play()
    }
}

let handleUserLeft = async (user) => {
    delete remoteUsers[user.uid]
}

let leaveAndRemoveLocalStream = async () => {
    for (let i=0; localTracks.length > i; i++){
        localTracks[i].stop()
        localTracks[i].close()
    }

    await client.leave()
    //This is somewhat of an issue because if user leaves without actaull pressing leave button, it will not trigger
    deleteMember()
}

/*-------------- MIC TOGGLE -----------------*/
var muteBtn = document.getElementById("muteBtn");
var unmuteBtn = document.getElementById("unmuteBtn");
var muteTxt = document.getElementById("muteTxt");

let member_name = document.getElementById("displayNameValue").innerHTML;
var microphoneDIV = document.getElementById(member_name);

function muteFunction() {
    console.log('TOGGLE MIC TRIGGERED')
    if(muteBtn.style.display == "block") {
        muteBtn.style.display = "none";
        unmuteBtn.style.display = "block";
        muteTxt.innerHTML = "unmute";

        microphoneDIV.querySelector('#muteStatus').style.display = "none";
        microphoneDIV.querySelector('#unmuteStatus').style.display = "block";

        localTracks[0].setMuted(false)
    }
    else {
        muteBtn.style.display = "block";
        unmuteBtn.style.display = "none";
        muteTxt.innerHTML = "mute";

        microphoneDIV.querySelector('#muteStatus').style.display = "block";
        microphoneDIV.querySelector('#unmuteStatus').style.display = "none";

        localTracks[0].setMuted(true)
    }
}

// function toggleMic() {
//     console.log('TOGGLE MIC TRIGGERED')
//         if(localTracks[0].muted) {
//             localTracks[0].setMuted(false)
//         }else {            
//             localTracks[0].setMuted(true)
//         }
// }


/*-------------- DEAFEN --------------*/
var deafenBtn = document.getElementById("deafenBtn");
var undeafenBtn = document.getElementById("undeafenBtn");
var deafenTxt = document.getElementById("deafenTxt");

var hearingDIV = document.getElementById(member_name);

function deafenFunction() {
    if(deafenBtn.style.display == "block") {
        deafenBtn.style.display = "none";
        undeafenBtn.style.display = "block";
        deafenTxt.innerHTML = "undeafen";

        hearingDIV.querySelector('#deafenStatus').style.display = "none";
        hearingDIV.querySelector('#undeafenStatus').style.display = "block";
    }
    else {
        deafenBtn.style.display = "block";
        undeafenBtn.style.display = "none";
        deafenTxt.innerHTML = "deafen";

        hearingDIV.querySelector('#deafenStatus').style.display = "block";
        hearingDIV.querySelector('#undeafenStatus').style.display = "none";
    }
}


let createMember = async () => {
    let response = await fetch('/Space/create_member/', {
        method:'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'name':NAME, 'room_name':CHANNEL, 'UID':UID})
    })
    let member = await response.json()
    return member
}


let getMember = async (user) => {
    let response = await fetch('/Space/get_member/?'+`UID=${user.uid}&room_name=${CHANNEL}`)
    let member = await response.json()
    return member
}

let deleteMember = async () => {
    let response = await fetch('/Space/delete_member/', {
        method:'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'name':NAME, 'room_name':CHANNEL, 'UID':UID})
    })
    let member = await response.json()
}


joinAndDisplayLocalStream()

document.getElementById('leaveBtn').addEventListener('click', leaveAndRemoveLocalStream)