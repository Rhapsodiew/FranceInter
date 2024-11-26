import api from "../api"
import { IText } from "@/app/shared/interfaces"

export const translate = async (text: IText) => {
    // console.log(text)
    const data_text =  await api.post('/translate', 
        {
        "msg": text.msg,
        "translated":text.translated,
        "ppl": text.ppl,
        "lang":text.lang
    })
    return data_text.data
}