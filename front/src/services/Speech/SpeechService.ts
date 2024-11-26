import api from "../api"
import { IText } from "@/app/shared/interfaces"

export const text_to_speech = async (data: IText) => {
    // console.log(data)
    const speech = await api.post('/speech', 
        {
        "msg": data.msg,
        "translated": data.translated,
        "lang": data.lang
    })
    return speech
}