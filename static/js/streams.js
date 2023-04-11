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
    localTracks[1].setMuted(true)

    let member = await createMember()

    // let player = `<div  class="video-container" id="user-container-${UID}">
    //                  <div class="video-player" id="user-${UID}"></div>
    //                  <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
    //               </div>`
    
    // document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)
    // localTracks[1].play(`user-${UID}`)
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


let toggleMic = async (e) => {
    console.log('TOGGLE MIC TRIGGERED')
    if(localTracks[0].muted){
        document.getElementById("unmuteStatus").style.display = "block"
        document.getElementById("muteStatus").style.display = "none"

        // document.getElementById("unmuteBtn").style.display = "block"
        // document.getElementById("muteBtn").style.display = "none"

        await localTracks[0].setMuted(false)
    }else{
        document.getElementById("unmuteStatus").style.display = "block"
        document.getElementById("muteStatus").style.display = "none"

        // document.getElementById("unmuteBtn").style.display = "block"
        // document.getElementById("muteBtn").style.display = "none"

        await localTracks[0].setMuted(true)
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
document.getElementById('muteBtn').addEventListener('click', toggleMic)