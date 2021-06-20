import streamlit as st
import tempfile
import warnings
import os
from PIL import Image


warnings.filterwarnings("ignore", message=r"Passing", category=FutureWarning)


# hide hamburger menu
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# hide footer
hide_footer_style = """
<style>
.reportview-container .main footer {visibility: hidden;}    
"""
st.markdown(hide_footer_style, unsafe_allow_html=True)


# files = [f for f in os.listdir("./encoded_images") if os.path.isfile(os.path.join("./encoded_images", f))]
files = ['bannister 293.jpg', 'bannister 294.jpg', 'bannister 303.jpg', 'bannister 304.jpg', 'bannister 306.jpg', 'bannister 317.jpg', 'bannister 318.jpg', 'bannister 319.jpg', 'bullet_train 231.jpg', 'cab 25.jpg', 'cab 255.jpg', 'cab 256.jpg', 'cab 26.jpg', 'cab 260.jpg', 'cab 27.jpg', 'cab 28.jpg', 'cab 286.jpg', 'cab 29.jpg', 'cab 30.jpg', 'cab 31.jpg', 'cab 32.jpg', 'cab 33.jpg', 'cab 34.jpg', 'cab 35.jpg', 'cab 36.jpg', 'cab 37.jpg', 'cab 38.jpg', 'cab 39.jpg', 'cab 40.jpg', 'cab 41.jpg', 'cab 42.jpg', 'cab 43.jpg', 'cab 44.jpg', 'cab 45.jpg', 'cab 46.jpg', 'cab 47.jpg', 'cab 48.jpg', 'cab 49.jpg', 'cab 50.jpg', 'cab 51.jpg', 'cab 52.jpg', 'cab 53.jpg', 'cab 54.jpg', 'cab 55.jpg', 'cab 56.jpg', 'cab 57.jpg', 'cab 58.jpg', 'cab 59.jpg', 'cab 60.jpg', 'cab 62.jpg', 'cab 63.jpg', 'cab 64.jpg', 'cab 65.jpg', 'cab 66.jpg', 'cab 67.jpg', 'cab 68.jpg', 'cab 69.jpg', 'cab 70.jpg', 'cab 71.jpg', 'cab 72.jpg', 'cab 73.jpg', 'cab 74.jpg', 'cab 75.jpg', 'cab 76.jpg', 'cab 77.jpg', 'cab 78.jpg', 'cab 79.jpg', 'cab 80.jpg', 'cab 81.jpg', 'cab 82.jpg', 'cab 83.jpg', 'cab 84.jpg', 'cab 85.jpg', 'cab 86.jpg', 'cab 87.jpg', 'cab 88.jpg', 'cab 89.jpg', 'car_mirror 261.jpg', 'car_mirror 262.jpg', 'car_mirror 268.jpg', 'car_mirror 292.jpg', 'car_mirror 94.jpg', 'dam 163.jpg', 'dam 167.jpg', 'dam 168.jpg', 'dam 169.jpg', 'dam 170.jpg', 'dam 171.jpg', 'dam 172.jpg', 'dam 173.jpg', 'dam 174.jpg', 'dam 176.jpg', 'dam 177.jpg', 'dam 179.jpg', 'limousine 102.jpg', 'limousine 103.jpg', 'limousine 105.jpg', 'limousine 106.jpg', 'limousine 107.jpg', 'limousine 108.jpg', 'limousine 109.jpg', 'limousine 111.jpg', 'limousine 114.jpg', 'limousine 116.jpg', 'limousine 117.jpg', 'limousine 182.jpg', 'limousine 184.jpg', 'limousine 185.jpg', 'limousine 186.jpg', 'limousine 187.jpg', 'limousine 188.jpg', 'limousine 189.jpg', 'limousine 191.jpg', 'limousine 196.jpg', 'limousine 197.jpg', 'limousine 198.jpg', 'limousine 201.jpg', 'limousine 202.jpg', 'limousine 203.jpg', 'limousine 204.jpg', 'limousine 205.jpg', 'limousine 206.jpg', 'limousine 207.jpg', 'limousine 208.jpg', 'limousine 209.jpg', 'limousine 211.jpg', 'limousine 212.jpg', 'limousine 213.jpg', 'limousine 215.jpg', 'limousine 216.jpg', 'limousine 217.jpg', 'limousine 218.jpg', 'limousine 223.jpg', 'limousine 224.jpg', 'limousine 248.jpg', 'limousine 249.jpg', 'limousine 251.jpg', 'limousine 252.jpg', 'limousine 253.jpg', 'limousine 257.jpg', 'limousine 259.jpg', 'limousine 281.jpg', 'limousine 284.jpg', 'limousine 291.jpg', 'limousine 92.jpg', 'limousine 97.jpg', 'matchstick 321.jpg', 'matchstick 322.jpg', 'matchstick 323.jpg', 'matchstick 324.jpg', 'matchstick 325.jpg', 'matchstick 326.jpg', 'matchstick 327.jpg', 'racer 110.jpg', 'racer 112.jpg', 'racer 113.jpg', 'racer 118.jpg', 'racer 119.jpg', 'racer 120.jpg', 'racer 121.jpg', 'racer 122.jpg', 'racer 123.jpg', 'racer 124.jpg', 'racer 125.jpg', 'racer 127.jpg', 'racer 128.jpg', 'racer 129.jpg', 'racer 131.jpg', 'racer 134.jpg', 'racer 135.jpg', 'racer 136.jpg', 'racer 137.jpg', 'racer 150.jpg', 'racer 151.jpg', 'racer 154.jpg', 'racer 155.jpg', 'racer 160.jpg', 'racer 214.jpg', 'racer 219.jpg', 'racer 220.jpg', 'racer 221.jpg', 'racer 222.jpg', 'racer 225.jpg', 'racer 226.jpg', 'racer 227.jpg', 'racer 258.jpg', 'racer 276.jpg', 'racer 277.jpg', 'racer 279.jpg', 'racer 280.jpg', 'racer 282.jpg', 'racer 283.jpg', 'racer 285.jpg', 'racer 287.jpg', 'racer 288.jpg', 'racer 289.jpg', 'racer 290.jpg', 'rule 310.jpg', 'rule 312.jpg', 'rule 315.jpg', 'rule 316.jpg', 'suspension_bridge 228.jpg', 'suspension_bridge 229.jpg', 'suspension_bridge 230.jpg', 'suspension_bridge 232.jpg', 'suspension_bridge 233.jpg', 'suspension_bridge 234.jpg', 'suspension_bridge 235.jpg', 'suspension_bridge 236.jpg', 'suspension_bridge 237.jpg', 'suspension_bridge 238.jpg', 'suspension_bridge 239.jpg', 'suspension_bridge 240.jpg', 'suspension_bridge 241.jpg', 'suspension_bridge 242.jpg', 'suspension_bridge 243.jpg', 'suspension_bridge 244.jpg', 'suspension_bridge 245.jpg', 'suspension_bridge 246.jpg', 'suspension_bridge 247.jpg', 'suspension_bridge 250.jpg', 'suspension_bridge 254.jpg', 'suspension_bridge 295.jpg', 'suspension_bridge 296.jpg', 'suspension_bridge 297.jpg', 'suspension_bridge 298.jpg', 'suspension_bridge 299.jpg', 'suspension_bridge 300.jpg', 'suspension_bridge 301.jpg', 'suspension_bridge 302.jpg', 'suspension_bridge 305.jpg', 'suspension_bridge 307.jpg', 'suspension_bridge 308.jpg', 'suspension_bridge 309.jpg', 'suspension_bridge 311.jpg', 'suspension_bridge 313.jpg', 'suspension_bridge 314.jpg', 'tow_truck 115.jpg', 'tow_truck 263.jpg', 'tow_truck 264.jpg', 'tow_truck 265.jpg', 'tow_truck 266.jpg', 'tow_truck 267.jpg', 'tow_truck 269.jpg', 'tow_truck 270.jpg', 'tow_truck 271.jpg', 'tow_truck 272.jpg', 'tow_truck 273.jpg', 'tow_truck 274.jpg', 'tow_truck 275.jpg', 'tow_truck 278.jpg', 'trailer_truck 0.jpg', 'trailer_truck 1.jpg', 'trailer_truck 10.jpg', 'trailer_truck 100.jpg', 'trailer_truck 101.jpg', 'trailer_truck 104.jpg', 'trailer_truck 11.jpg', 'trailer_truck 12.jpg', 'trailer_truck 126.jpg', 'trailer_truck 13.jpg', 'trailer_truck 130.jpg', 'trailer_truck 132.jpg', 'trailer_truck 133.jpg', 'trailer_truck 138.jpg', 'trailer_truck 139.jpg', 'trailer_truck 14.jpg', 'trailer_truck 140.jpg', 'trailer_truck 141.jpg', 'trailer_truck 142.jpg', 'trailer_truck 143.jpg', 'trailer_truck 144.jpg', 'trailer_truck 146.jpg', 'trailer_truck 147.jpg', 'trailer_truck 148.jpg', 'trailer_truck 149.jpg', 'trailer_truck 15.jpg', 'trailer_truck 152.jpg', 'trailer_truck 153.jpg', 'trailer_truck 156.jpg', 'trailer_truck 157.jpg', 'trailer_truck 158.jpg', 'trailer_truck 159.jpg', 'trailer_truck 16.jpg', 'trailer_truck 161.jpg', 'trailer_truck 162.jpg', 'trailer_truck 164.jpg', 'trailer_truck 165.jpg', 'trailer_truck 166.jpg', 'trailer_truck 17.jpg', 'trailer_truck 175.jpg', 'trailer_truck 178.jpg', 'trailer_truck 18.jpg', 'trailer_truck 180.jpg', 'trailer_truck 181.jpg', 'trailer_truck 183.jpg', 'trailer_truck 19.jpg', 'trailer_truck 190.jpg', 'trailer_truck 192.jpg', 'trailer_truck 193.jpg', 'trailer_truck 194.jpg', 'trailer_truck 195.jpg', 'trailer_truck 199.jpg', 'trailer_truck 2.jpg', 'trailer_truck 20.jpg', 'trailer_truck 200.jpg', 'trailer_truck 21.jpg', 'trailer_truck 210.jpg', 'trailer_truck 22.jpg', 'trailer_truck 23.jpg', 'trailer_truck 24.jpg', 'trailer_truck 3.jpg', 'trailer_truck 4.jpg', 'trailer_truck 5.jpg', 'trailer_truck 6.jpg', 'trailer_truck 61.jpg', 'trailer_truck 7.jpg', 'trailer_truck 8.jpg', 'trailer_truck 9.jpg', 'trailer_truck 90.jpg', 'trailer_truck 91.jpg', 'trailer_truck 93.jpg', 'trailer_truck 95.jpg', 'trailer_truck 96.jpg', 'trailer_truck 98.jpg', 'trailer_truck 99.jpg', 'trolleybus 145.jpg', 'wing 320.jpg']
fi = [i.split()[0] for i in files] 
detected_obj = list(set(fi))

def play_video(vid_path):
    # video_file = open(vid_path, 'rb')
    # video_bytes = video_file.read()
    st.video(vid_path)
  

def filter_frame(txt_search):
#     files = [f for f in os.listdir("./encoded_images") if os.path.isfile(os.path.join("./encoded_images", f))]
    files.sort(key = lambda x: int(x.split()[1][:-4]))
    indices = [i for i, s in enumerate(files) if txt_search.lower() in s]
    return files[indices[0]]


def main():
    global rez

    rez = "..."

    st.sidebar.title("Dashboard")

    home = st.sidebar.button('Home', key='home')
    upload = st.sidebar.button('Upload video',key='upload')


    if upload:
        f = st.file_uploader("Upload video")

        s1, s2, s3 = st.beta_columns([1,4,2])

        with s2:
            search = st.text_input("Search for objects in video")
            if search in detected_obj:
                rez = "Found"
            else:
                rez = "Not Found"
        
        with s3:
            st.write('Search results')
            if f is None:
                status = st.write(f'{search} ...')
            else:
                status = st.write(f'{search} {rez}')


        with st.beta_container():

            col1, col2 = st.beta_columns([2,6])

            

            with col2:

                if f is not None:
                    tfile = tempfile.NamedTemporaryFile(delete=False) 
                    tfile.write(f.read())


                    with col1:
                        st.write("Objects in video")
                        for i in range(len(detected_obj)):
                            st.write(str(i+1) +  " "+str(detected_obj[i]))

                 

    else:

        st.title('Object(s) Detection in video')

        hs1, hs2, hs3 = st.beta_columns([1,4,2])

        with hs2:
            h_search = st.text_input("Search for objects in video")
            if h_search.lower() in detected_obj:
                rez = "found"
            else:
                rez = "not found"
        
        with hs3:
            st.write('Search results')
            if h_search.lower() is None:
                status = st.write(f'{h_search} ...')
            else:
                status = st.write(f'{h_search} {rez}')


        if len(detected_obj) > 6:
            col1, col2, col3 = st.beta_columns([2,2,6])
            with col1:
                st.subheader("Objects in video")
                for i in range(0,7):
                    st.write(str(i+1) +  " "+str(detected_obj[i]))
            with col2:
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                for i in range(7,len(detected_obj)-1):
                    st.write(str(i+1) +  " "+str(detected_obj[i]))
            with col3:
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                if h_search.lower() in detected_obj:
                    rez = "found"
                    img = Image.open('./encoded_images/'+str(filter_frame(h_search)))
                    st.image(img, caption=h_search.lower() + " frame found")
                else:
                    play_video("https://youtu.be/oGMQacLTr3U")
        else:
            col1, col2 = st,beta_columns([2,6])
            with col1:  
                st.write("Objects in video")
                for i in range(len(detected_obj)):
                    st.write(str(i+1) +  " "+str(detected_obj[i]))
            with col2:
                play_video("https://youtu.be/oGMQacLTr3U")
    
                    

    # else:
    #     st.title('Object Detection using VGG16 Model...')

    #     c1, c2, c3 = st.beta_columns([4,2,4])
    #     with c2:
    #         st.write('Done by:')

    #     b1,m1,l1 = st.beta_columns([3,1,3])
    #     with b1:
    #         st.write('Blessed Mutengwa - R182565F')
    #         st.write('blessedmutengwa@gmail.com')
    #     with m1:
    #         st.write("|")
    #     with l1:
    #         st.write('Linval Chisoko - R182565F')
    #         st.write('linvaltchisoko@gmail.com')
    


if __name__ == '__main__':
    main()
