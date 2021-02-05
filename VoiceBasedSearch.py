import speech_recognition as sr
import webbrowser as wb

def voiceRecogAnSearch():
    recog = sr.Recognizer()
    with sr.Microphone() as micSrc:
    #    print("\n ###> Speak something to test: ");
    #    print(' ########> Your words are: <%s>.'%recog.recognize_google(recog.listen(micSrc)))
        print("\n ###> Where do you wanna search: ");
        audio1 = recog.listen(micSrc)
        try:
            #srcSearch = recog.recognize_google(audio1)
            srcSearch = recog.recognize_google(audio1)
            print(' ########> Attempting to search <%s>.'%srcSearch)
            if srcSearch == 'Google':
                srcURL = 'https://www.google.com/search?q='
            if srcSearch == 'YouTube':
                srcURL = 'https://www.youtube.com/results?search_query='
            with sr.Microphone() as micSrc:
                print("\n ###> What do you wanna search in "+srcSearch+": ");
                audio2 = recog.listen(micSrc)
                try:
                    finalURL = srcURL+recog.recognize_google(audio2)
                    print(' ########> Attempting to open the URL <%s>.'%finalURL)
                    wb.get().open_new(finalURL)
                except sr.UnknownValueError:
                    print(" ###> UNKNOWN ERROR");
                except sr.RequestError as err:
                    print(" ###> REQUEST ERROR : "+format(err));
        except sr.UnknownValueError:
            print(" ###> UNKNOWN ERROR");
        except sr.RequestError as err:
            print(" ###> REQUEST ERROR : "+format(err));


if __name__ == '__main__':
    voiceRecogAnSearch()
