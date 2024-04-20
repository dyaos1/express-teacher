interface ServerStatus {
    status: boolean
}

export default function ConSensor({status}: ServerStatus) {
    const text = status ? 'connected' : 'disconnected'
    let style = "flex p-1"
    status ? (style += " text-green-400") : (style+= " text-red-400")
    return (
        <div className="flex flex-row">
            <span className="flex p-1">
                <p>server status:</p>
            </span>
            <span className={style}>
                <p>{text}</p>
            </span>
        </div>
    )
}