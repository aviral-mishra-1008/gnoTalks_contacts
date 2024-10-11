# GnoTalks Contact Database - Instruction Manual

![Screenshot_2024-10-05_150356-pixelAI](https://github.com/user-attachments/assets/d0d5b1fe-dadd-404f-97da-b5cff7016dda)


## Introduction
The GnoTalks Contact Database is a vital resource designed to manage the details of speakers who were invited to GnoTalks at MNNIT but couldn't attend due to various reasons. By maintaining and updating this database, future teams can save significant time and effort in research, ensuring continuity and efficiency in inviting speakers. This resource benefits not only the current team but also future teams long after we've left MNNIT, as they won't need to redo the same research to fetch contacts.

**NOTE: It is important to firstly get access to gnotalks database file and encryption pass file from authorized entities within the institute**

## Why Use This Database?
- **Efficient Tracking**: Keep a record of invited speakers who haven't yet visited.
- **Ease of Access**: Quickly fetch speaker details when planning future events.
- **Data Security**: Utilizes encryption to securely store sensitive information such as phone numbers.
- **Deletion**: Easily delete records of speakers once they visit.

## Streamlit Apps
There are three Streamlit apps provided to manage the database:
1. **add_contacts**: Add new contacts to the database.
2. **fetch_contacts**: Fetch and display contacts based on the input name.
3. **delete_contacts**: Delete contacts based on their ID.

### Adding Contacts
To add new contacts, run the `add_contacts` Streamlit app. This app will prompt you to enter the speaker details to be added to the database.

### Fetching Contacts
To fetch and display contacts, run the `fetch_contacts` Streamlit app. This app will prompt you for the name of the speaker to search for. It will then display all matching records with their details.

### Deleting Contacts
To delete contacts, run the `delete_contacts` Streamlit app. This app will prompt you for the name of the speaker to search for. It will then display all matching records with their IDs and ask you to enter the IDs of the records to be deleted.

## Running the Streamlit Apps
1. **Ensure you have all the required libraries installed**. You can install them using:
   ```bash
   pip install -r requirements.txt

2. **Run the Streamlit app** for adding contacts:
    ```bash
    streamlit run add_contacts.py
    
3. **Run the Streamlit app** for fetching contacts:
    ```bash
    streamlit run fetch_contacts.py

4. **Run the Streamlit app** for deleting contacts:
    ```bash
    streamlit run delete.py

## Getting the Encryption Key and Database File
- **Encryption Key:** Contact the GnoTalks team seniors to get the encryption key file. This key is necessary to encrypt and decrypt phone numbers.

- **Database File:** Contact the current GnoTalks team seniors to get access to the database file gnoTalks_contactBase.db.

- **Storing Files:** Store both the encryption key file .gnotalks and the database file gnoTalks_contactBase.db in the root directory where the Streamlit apps are located.

## Regular Updates
It's crucial to regularly update the database with new contacts. At the end of each term, ensure that an updated version of the database is sent to the next team. This ensures the continuity and relevance of the database, benefiting future teams and maintaining the efficiency of GnoTalks.

For any queries or issues, please reach out to the GnoTalks team seniors or mail me at aviralmishra10@gmail.com
