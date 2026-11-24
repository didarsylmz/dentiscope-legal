# Denstrument AI – Privacy Policy

Last updated: November 2026

Denstrument AI (“Denstrument”, “we”, “our”, or “us”) respects your privacy and is committed to protecting your information. This Privacy Policy explains how Denstrument AI handles information when you use our mobile application and related services. Denstrument AI was previously named Dentiscope AI.

By using Denstrument AI, you agree to the practices described in this Privacy Policy.

## 1. Information We Process

Denstrument AI is designed to minimize personal data collection.

Users are not required to create an account in order to use the application.

We do not intentionally collect personally identifiable information such as:

• Full name  
• Home address  
• Phone number  
• Government-issued identification  
• Personal health records

The limited information that is processed is described in the sections below.

## 2. Scan Images and AI Processing

When you use the scan feature, the photo you take or select is reduced in size on your device and sent over an encrypted (HTTPS) connection to our server, where it is processed by an AI model to recognize the dental instrument.

• Scan images are not used to identify users.  
• Scan images are processed temporarily and deleted immediately after processing. They are not permanently stored on our servers.  
• Scan images are not used for dataset collection or machine learning training.

If we ever introduce an optional feature that uses images to improve the service, it will only work with your explicit consent and this policy will be updated before it is introduced.

## 3. Device and App Integrity Verification

To protect the service against abuse and unauthorized or modified copies of the app, Denstrument AI uses Firebase App Check, which relies on Google Play Integrity on Android and Apple App Attest on iOS.

These services confirm that requests come from a genuine copy of the app running on a genuine device. They process technical device and app information (such as device and operating system type, app identifier and an attestation token). This information is used only for security and is not used to identify you personally.

## 4. Server and Network Logs

When the app communicates with our server (for example to analyze a scan or to check whether an app update is required), our server application does not write your IP address to its logs. Its logs contain only technical events such as the time of a request, whether the app integrity check passed and whether the request succeeded.

Your IP address is used in memory only, to limit the number of requests per network address and protect the service against abuse. It is not stored by our server application.

**Premium content requests (from app version 1.3.0).** When a subscriber opens premium content, the app sends our server the anonymous app user identifier (see Section 6) so that the subscription can be checked. Our server does not write this identifier to its logs; it logs only the type of content and whether the request succeeded. To enforce the daily limit, it counts requests in memory under a salted, one-way hash of the identifier, and these counts are cleared every day. If an account downloads an unusually large amount of premium content, reaches the daily limit or is suspended, the log records only a short part of that hash, so that bulk copying can be detected.

Our hosting provider’s infrastructure may process standard technical request information, including IP addresses, as part of operating and protecting the service. This is kept only for a limited period in accordance with the hosting provider’s log retention.

## 5. Local Device Storage

Certain application data is stored locally on your device in order to provide the application’s features, including:

• Favorites  
• Scan history  
• Cached premium access status  
• Daily free-usage counters  
• Usage streak information (used to decide when to show a rating request or a premium invitation)  
• Learning progress (unlocked cards and questions, self-test attempts, oral exam prep marks)  
• Your analytics choice and other app preferences  
• Premium content you have opened (from app version 1.3.0), stored encrypted with a key kept in the device’s secure storage (Android Keystore / iOS Keychain). It is refreshed after 7 days, removed after 30 days, and deleted when your subscription ends.  
• Technical settings sent by our server (for example whether a screen protection feature is turned on)

This information remains on your device and is not shared by Denstrument AI.

## 6. Premium Purchases and Subscriptions

Denstrument AI offers premium subscription features through Google Play and the Apple App Store.

Payment transactions are processed by the respective platform providers. Denstrument AI does not collect or store payment card information.

Subscription status is managed through RevenueCat, which receives purchase and subscription information from the app stores together with an anonymous app user identifier, so that premium access can be verified, restored and kept up to date. This identifier does not include your name or contact details.

Our server also uses this anonymous identifier to check your subscription with RevenueCat before it sends premium content or processes a scan. If RevenueCat cannot be reached for a short time, a subscription confirmed within the previous 24 hours is accepted, so that a brief outage does not interrupt access.

**Terms confirmation.** Before a purchase, the app asks you to confirm the Terms of Use, including the Premium section. The version of the Terms and the time of your confirmation are stored as attributes of your anonymous subscription record at RevenueCat, so that we can show which Terms applied to your subscription.

**Content watermark.** Premium content shows a faint short code derived from a one-way hash of your anonymous identifier. It cannot be turned back into the identifier by others, and we use it only to find the source of leaked premium content.

## 7. Analytics and Crash Reporting

Denstrument AI uses Firebase Crashlytics to detect and fix crashes, and Firebase Analytics to understand which features are used.

**Analytics only with your consent.** Firebase Analytics is turned off until you allow it. The first time you open the app, it asks whether you want to share usage data. If you decline, every feature keeps working the same. You can change your choice any time in Settings → Share usage data.

**Crash reports** are always sent, because they are needed to keep the app working.

These services may collect limited technical information, including:

• Device model  
• Operating system version  
• App version  
• Usage events, such as which screens are opened, quiz answers and whether premium content was loaded from the device or the server (Analytics, only with your consent)  
• Crash diagnostics

They do not include your name, e-mail address or location. This information is used solely for improving the application and maintaining service stability.

## 8. Ratings and App Updates

• Rating requests are shown using the native rating dialog provided by Apple or Google. Any rating or review you submit is handled by the respective app store.  
• When the app starts, it may check with our server whether your app version is still supported. No personal information is sent as part of this check.

## 9. Service Providers

We rely on the following service providers to operate Denstrument AI. Each processes information only as needed to provide its service and under its own privacy policy:

• Google (Firebase Analytics, Firebase Crashlytics, Firebase App Check, Google Play)  
• Apple (App Store, App Attest)  
• RevenueCat (subscription management)  
• Render (hosting of our recognition server)

These providers may process information in countries other than your own.

Users in Türkiye: a Turkish privacy notice under the Personal Data Protection Law No. 6698 (KVKK) is available at [KVKK Aydınlatma Metni](kvkk-aydinlatma.html).

## 10. Educational Use Disclaimer

Denstrument AI is intended solely for educational, informational, and reference purposes.

The application does not provide medical diagnosis, treatment recommendations, or professional clinical decision-making services.

AI-generated predictions may occasionally be inaccurate.

Denstrument AI does not guarantee the accuracy, completeness, or reliability of AI-generated predictions or educational content.

Users should not rely solely on application results for clinical or professional decisions.

## 11. Limitation of Liability

To the maximum extent permitted by applicable law, Denstrument AI shall not be held responsible for any clinical, educational, professional, financial, or other decisions made based on information provided by the application.

Use of the application is at the user’s own discretion and responsibility.

## 12. Data Security

We take reasonable technical and organizational measures intended to help protect information processed by the application, including encrypted connections and device and app integrity verification.

However, no method of electronic transmission, storage, or internet-based communication can be guaranteed to be completely secure.

## 13. Children’s Privacy

Denstrument AI is not specifically directed toward children under the age of 13.

If you believe that a child has provided personal information through the application, please contact us so appropriate action may be taken.

## 14. Data Retention

Denstrument AI is designed to minimize data retention.

• Scan images submitted for AI recognition are processed temporarily and are deleted immediately after processing. They are not permanently stored on our servers.  
• Server and network logs are kept only for a limited period, as described in Section 4. Daily premium request counts are kept in memory and cleared every day.  
• Premium content stored on your device is deleted after 30 days at the latest, or when your subscription ends.  
• Your Terms confirmation is kept with your anonymous subscription record at RevenueCat for as long as that record exists.  
• Scan history, favorites, cached premium status, usage counters and application preferences are stored locally on your device.  
• Analytics, crash reporting and subscription information may be retained by our service providers only for as long as necessary to provide their services, in accordance with their own privacy policies.

## 15. Data Deletion

Because Denstrument AI does not require users to create an account, we maintain very limited personal data.

• Data stored locally on your device is removed when you delete the app or clear its data.  
• You may request deletion of any personal information associated with communications sent to Denstrument AI (such as support emails) by contacting the address below.

We will review and process legitimate deletion requests within a reasonable period in accordance with applicable laws.

Scan images are deleted immediately after processing. Therefore, no deletion request is required for scan images.

## 16. Changes to This Policy

We may update this Privacy Policy from time to time.

Updated versions will be reflected by the "Last updated" date shown at the top of this document.

Continued use of the application after changes become effective constitutes acceptance of the updated policy.

## 17. Contact

If you have questions regarding this Privacy Policy or Denstrument AI, you may contact:

Denstrument AI Support  
denstrumentai@gmail.com
