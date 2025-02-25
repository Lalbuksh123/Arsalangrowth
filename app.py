import streamlit as st

st.set_page_config(page_title= "growth mindset project", page_icon="★")

st.title("Growth Mindset Challange: Web App With Streamlit")

st.header("🚀Wellcome To Your Growth Journey!")

st.write("Embrance Challanges, learn from mistake,and unlock your full potential. This AI-powered app help you build a growth mind set with reflection , challanges and achievement!🌟")

#quotes section 

st.header(" 💡 Today's Growth Mindset Quotes")
st.write("Success is not final, failure is not fatal:it is the courage to continue that counts._Wistom Churchill")

st.header("What Your Challange Today?")
user_input = st.text_input("Describe a challange you're facing:")

#Condition...........
if user_input:
    st.success(f"you're facing{user_input}. keep pushing forward towards your goals")
else:("Tell us about your challangeto get started!")


#reflexing...............
st.header("Reflection On Your Learning")
reflection = st.text_area("Write Your Reflection Here:")

if reflection:
    st.success(f"🌟Greate Insigth! Your Reflection: {reflection} ")
else:
        st.info("Reflection on past experience help you grow! Share your deficulties")

        #achievement..........
        st.header(f"Celebrating Your Win!")
        achievement= st.text_input("Share omething You're recently accompllished")

        if achievement:
            st.success(f"🌠Amazing! You achieved:{achievement}")
        else:
                st.info("Big or small , every achievement counts! share one now😍")

                #footer

                st.write("- - -")
                st.write("🚀Keep believing in yourself. Growth is a journey , not a destinaton !☀️")
                st.write("**⛔ Created by Lal Buksh Shaikh**")
