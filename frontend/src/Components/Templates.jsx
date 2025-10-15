import Dock from "../Components/Dock.jsx"

export default function Templates({children}){
    return (
    <div class="min-h-screen flex flex-col justify-between">
        <div class="flex-grow">
            {children}
        </div>
 
        <Dock />
    </div>
    )
}
