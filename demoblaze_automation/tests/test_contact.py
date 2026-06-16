import pytest
from demoblaze_automation.pages.home_page import HomePage
from demoblaze_automation.globals import BASE_URL

def test_contact_form_submission(page):
    home_page = HomePage(page)
    page.goto(BASE_URL)

    # Click Contact button to open modal
    home_page.click_contact()
    
    # Wait for the modal to be visible
    page.wait_for_selector("#exampleModal", state="visible")

    # Fill in fake details
    home_page.contact_email_field.fill("fake_user@example.com")
    home_page.contact_name_field.fill("Fake User")
    home_page.contact_message_field.fill("This is a automated test message.")

    # Prepare to handle the success alert
    # The message shown is "Thanks for the message!!"
    actual_alert_message = []
    def handle_dialog(dialog):
        actual_alert_message.append(dialog.message)
        dialog.accept()

    page.once("dialog", handle_dialog)

    # Click Send Message
    home_page.send_message_button.click()

    # Verify the alert message
    assert len(actual_alert_message) > 0, "No alert was shown after sending message"
    assert actual_alert_message[0] == "Thanks for the message!!", f"Unexpected alert message: {actual_alert_message[0]}"
