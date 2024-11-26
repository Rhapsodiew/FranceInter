import api from "../api"
import { IImage } from "@/app/shared/interfaces"

export const find_people = async (data: IImage) => {
    // console.log(data)
    const more_ppl_than_accepted = await api.post('/vision', 
        {
        "path": data.path,
        "ppl": data.ppl,
    })
    return more_ppl_than_accepted.data
}