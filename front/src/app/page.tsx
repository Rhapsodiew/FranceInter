'use client'
import { useState } from "react";
import { IImage, IText } from "./shared/interfaces";
import { find_people } from "@/services/Visage/VisageService";
import { translate } from "@/services/Translate/TranslateService";
import { text_to_speech } from "@/services/Speech/SpeechService";

export default function Home() {

  const [textData, setTextData] = useState<IText> ({
    msg: '',
    translated:'',
    ppl:0,
    lang:'en'
  })
  const [imgData, setImgData] = useState<IImage> ({
    path:'deux.jpeg',
    ppl:0
  })

  const handleTextDataChange = (data: React.ChangeEvent<HTMLInputElement>) => {
    const {name, value} = data.target;
    if (name === "path"){
      setImgData(prevData => ({... prevData, [name]: value}))
    } else if (name === "msg"){
      setTextData(prevData => ({... prevData, [name]: value}))
    } else if (name === "lang"){
      setTextData(prevData => ({... prevData, [name]: value}))
      console.log(textData)
    } else {
      setTextData(prevData => ({... prevData, [name]: value}))
      setImgData(prevData => ({... prevData, [name]: value}))
    }
  }

  const handleSubmit = async (data: React.ChangeEvent<HTMLInputElement>) => {
  data.preventDefault();
  try {
    const more_ppl_than_accepted =  await find_people(imgData)
    // console.log(more_ppl_than_accepted);    
    if (more_ppl_than_accepted) {
      const response = await translate(textData)
      // console.log('response',response);
      await text_to_speech(response)
    } 
  } catch (err) {
      console.error(err)
  }
}

  return (
    <div className="bg-slate-900 h-screen cursor-default">
      <div className="bg-indigo-950 text-indigo-50 font-extrabold text-2xl px-2 py-1 flex justify-center">
        <h1>BACKOFFICE</h1>  
      </div>
      <div className="flex justify-center">
        <form className="p-6 rounded-b-3xl bg-indigo-950 font-bold">
          <div>
            <label htmlFor="msg" className="text-lg text-indigo-50">base_msg</label>
            <br/>
            <input className="rounded-xl px-2" type="text" name="msg" id="msg" placeholder="base_msg" required minLength={3} 
            onChange={handleTextDataChange}value={textData.msg}/>
          </div>
          <br/>
          <div>
            <label htmlFor="image" className="text-lg text-indigo-50">Image</label>
            <br/>
            {/* <input className="rounded-xl px-2" type="text" name="path" id="path" placeholder="Image path" required minLength={2}
            onChange={handleTextDataChange}value={imgData.path}
            /> */}
            <select onChange={handleTextDataChange} defaultValue={"deux.jpeg"} id="path" name="path" className="rounded-xl px-2">
              <option value={"deux.jpeg"}>Deux</option>
              <option value={"trois.jpg"}>Trois</option>
              <option value={"quatre.jpg"}>Quatre</option>
              <option value={"sept.jpeg"}>Sept</option>
              <option value={"neuf.jpg"}>Neuf</option>

            </select>
          </div>
          <br/>
          <div>
            <label htmlFor="ppl" className="text-lg text-indigo-50">Nb</label>
            <br/>
            <input className="rounded-xl px-2" type="number" name="ppl" id="ppl" placeholder="Ppl allowed" required min={0}
            onChange={handleTextDataChange}value={imgData.ppl}
            />
          </div>
          <br />
          <div>
            <label htmlFor="ppl" className="text-lg text-indigo-50">Language</label>
            <br/>
            <div>
              <select onChange={handleTextDataChange} id="lang" name="lang" defaultValue={"en"} className="px-2 rounded-xl">
                <option value={"en"}>Anglais</option>
                <option value={"es"}>Espagnol</option>
                <option value={"it"}>Italien</option>
                <option value={"de"}>Allemand</option>
              </select>
            </div>
          </div>  
          <br />
          <div className="flex justify-center bg-indigo-900/75 hover:bg-indigo-900/50 p-2 mx-8 rounded-3xl">
            <button onClick={handleSubmit} className="text-lg text-indigo-50">Start</button>
          </div>
        </form>
        {/* <p>{textData.msg}, {imgData.path}, {imgData.ppl}, {textData.lang}</p> */}
      </div>
    </div>
  );
}