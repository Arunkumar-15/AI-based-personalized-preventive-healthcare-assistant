import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

const resources = {
  en: {
    translation: {
      nav: {
        brand: 'AI Healthcare Assistant',
        home: 'Home',
        about: 'About',
        contact: 'Contact',
        language: 'English',
        modelInfo: 'Model Info'
      },
      form: {
        title: 'Basic Health Assessment',
        subtitle: 'Please fill in the details below to check risk',
        privacyBadge: '100% Private & De-Identified Assessment',
        privacyMode: 'Privacy-Preserving Anonymized Storage (De-Identified via Token)',
        age: 'Age (Years)',
        gender: 'Gender',
        selectGender: 'Select Gender',
        male: 'Male',
        female: 'Female',
        other: 'Other',
        height: 'Height (cm)',
        weight: 'Weight (kg)',
        bmi: 'Calculated BMI',
        smoking: 'Smoking Habit',
        alcohol: 'Alcohol Consumption',
        yes: 'Yes',
        no: 'No',
        smokingFrequency: 'Frequency (Smoking)',
        alcoholFrequency: 'Frequency (Alcohol)',
        regular: 'Regular',
        occasional: 'Occasional',
        physicalActivity: 'Physical Activity',
        sedentary: 'Sedentary (Little or no exercise)',
        light: 'Light (1-3 days/week)',
        moderate: 'Moderate (3-5 days/week)',
        active: 'Active (6-7 days/week)',
        sleepHours: 'Average Sleep Duration (Hours/day)',
        familyHistory: 'Family Medical History (Select all that apply)',
        noneFamily: 'None / Nothing',
        heartDisease: 'Heart Disease',
        diabetes: 'Diabetes',
        hypertension: 'Hypertension',
        otherFamily: 'Other',
        symptoms: 'Symptoms',
        fatigue: 'Fatigue',
        chestPain: 'Chest Pain',
        shortnessOfBreath: 'Shortness of Breath',
        excessiveThirst: 'Excessive Thirst',
        frequentUrination: 'Frequent Urination',
        dizziness: 'Dizziness',
        headache: 'Headache',
        otherSymptom: 'Other Symptoms (Optional free text)',
        otherSymptomPlaceholder: 'Enter any other symptom...',
        submit: 'Submit',
        submitting: 'Analyzing with AI...',
        quickFill: 'Quick-Fill Demo Profiles:',
        healthyProfile: 'Healthy Profile',
        atRiskProfile: 'At-Risk Profile',
        highRiskProfile: 'High-Risk Profile'
      },
      output: {
        title: 'Health Assessment Result',
        subtitle: 'Based on your provided information',
        riskLevel: 'Risk Level:',
        lowRisk: 'Low Risk',
        moderateRisk: 'Moderate Risk',
        highRisk: 'High Risk',
        criticalRisk: 'Critical Risk',
        importantFactors: 'Important Factors',
        preventiveGuidance: 'Preventive Guidance',
        newAssessment: 'New Assessment',
        privacyCertificate: 'Data Privacy & Confidentiality Certificate',
        anonSessionId: 'Anonymous Session Token:',
        kAnonymityLabel: 'Data Protection Bracket:',
        complianceStandard: 'Compliance Standard:',
        zeroStorage: 'Anonymized Data Storage Secured (Stored via Cryptographic Token ANON-XXXX)',
        highRiskDesc: 'You may have a higher risk of developing health problems. It is recommended to take preventive action and consult a healthcare professional.',
        modRiskDesc: 'You may have a moderate risk of developing health problems. It is recommended to make positive lifestyle adjustments and monitor your health.',
        lowRiskDesc: 'Your risk indicators are currently within the healthy range. Continue to maintain balanced lifestyle and wellness habits.'
      }
    }
  },
  ta: {
    translation: {
      nav: {
        brand: 'AI சுகாதார உதவியாளர்',
        home: 'முகப்பு',
        about: 'விவரம்',
        contact: 'தொடர்பு',
        language: 'தமிழ்',
        modelInfo: 'மாதிரி தகவல்'
      },
      form: {
        title: 'அடிப்படை சுகாதார மதிப்பீடு',
        subtitle: 'உங்கள் உடல்நல அபாயத்தை அறிய கீழே உள்ள விவரங்களை நிரப்பவும்',
        privacyBadge: '100% தனிப்பட்ட மற்றும் பெயர் மறைக்கப்பட்ட மதிப்பீடு',
        privacyMode: 'பெயர் மறைக்கப்பட்ட குறியீட்டுடன் பாதுகாக்கப்பட்ட தரவு சேமிப்பு',
        age: 'வயது (ஆண்டுகள்)',
        gender: 'பாலினம்',
        selectGender: 'பாலினத்தைத் தேர்ந்தெடுக்கவும்',
        male: 'ஆண்',
        female: 'பெண்',
        other: 'மற்றவை',
        height: 'உயரம் (செ.மீ)',
        weight: 'எடை (கிலோ)',
        bmi: 'கணக்கிடப்பட்ட BMI',
        smoking: 'புகைபிடிக்கும் பழக்கம்',
        alcohol: 'மது அருந்தும் பழக்கம்',
        yes: 'ஆம்',
        no: 'இல்லை',
        smokingFrequency: 'புகைபிடிக்கும் அளவு / வகை',
        alcoholFrequency: 'மது அருந்தும் அளவு / வகை',
        regular: 'வழக்கமாக (Regular)',
        occasional: 'எப்போதாவது (Occasional)',
        physicalActivity: 'உடற்பயிற்சி நிலை',
        sedentary: 'செயலற்ற நிலை (உடற்பயிற்சி இல்லை)',
        light: 'குறைவான உடற்பயிற்சி (வாரத்திற்கு 1-3 நாட்கள்)',
        moderate: 'மிதமான உடற்பயிற்சி (வாரத்திற்கு 3-5 நாட்கள்)',
        active: 'தீவிர உடற்பயிற்சி (வாரத்திற்கு 6-7 நாட்கள்)',
        sleepHours: 'சராசரி தூக்க நேரம் (மணிநேரம்/நாள்)',
        familyHistory: 'குடும்ப மருத்துவ வரலாறு (பொருந்துவதை தேர்வு செய்க)',
        noneFamily: 'எதுவும் இல்லை (None)',
        heartDisease: 'இதய நோய்',
        diabetes: 'நீரிழிவு நோய்',
        hypertension: 'உயர் இரத்த அழுத்தம்',
        otherFamily: 'பிற நோய்கள்',
        symptoms: 'அறிகுறிகள் (Symptoms)',
        fatigue: 'உடல் சோர்வு (Fatigue)',
        chestPain: 'மார்பு வலி (Chest Pain)',
        shortnessOfBreath: 'மூச்சுத் திணறல் (Shortness of Breath)',
        excessiveThirst: 'அதிக தாகம் (Excessive Thirst)',
        frequentUrination: 'அடிக்கடி சிறுநீர் கழித்தல் (Frequent Urination)',
        dizziness: 'தலைசுற்றல் / மயக்கம் (Dizziness)',
        headache: 'தலைவலி (Headache)',
        otherSymptom: 'பிற அறிகுறிகள் (விருப்பப்பட்டால் எழுதவும்)',
        otherSymptomPlaceholder: 'பிற அறிகுறிகளை உள்ளிடவும்...',
        submit: 'மதிப்பீடு செய்க',
        submitting: 'AI மூலம் மதிப்பீடு செய்யப்படுகிறது...',
        quickFill: 'மாதிரி சுயவிவரங்கள் (டெமோ):',
        healthyProfile: 'ஆரோக்கியமான நபர்',
        atRiskProfile: 'மிதமான அபாய நபர்',
        highRiskProfile: 'அதிக அபாய நபர்'
      },
      output: {
        title: 'சுகாதார மதிப்பீட்டு முடிவு',
        subtitle: 'நீங்கள் வழங்கிய தகவலின் அடிப்படையில்',
        riskLevel: 'ஆபத்து நிலை:',
        lowRisk: 'குறைந்த ஆபத்து',
        moderateRisk: 'மிதமான ஆபத்து',
        highRisk: 'அதிக ஆபத்து',
        criticalRisk: 'தீவிர ஆபத்து',
        importantFactors: 'முக்கிய காரணிகள்',
        preventiveGuidance: 'தடுப்பு வழிகாட்டுதல்',
        newAssessment: 'புதிய மதிப்பீடு',
        privacyCertificate: 'தரவு தனியுரிமை மற்றும் இரகசியத்தன்மை சான்றிதழ்',
        anonSessionId: 'பெயர் மறைக்கப்பட்ட அமர்வு எண் (Token):',
        kAnonymityLabel: 'தரவு பாதுகாப்பு வரம்பு:',
        complianceStandard: 'தரநிலை:',
        zeroStorage: 'பெயர் மறைக்கப்பட்ட குறியீட்டு முறையில் பாதுகாப்பாக சேமிக்கப்பட்டது',
        highRiskDesc: 'உங்களுக்கு உடல்நலக் கோளாறுகள் ஏற்படும் அபாயம் அதிகமாக உள்ளது. தடுப்பு நடவடிக்கைகளை எடுத்து மருத்துவ ஆலோசனையைப் பெற பரிந்துரைக்கப்படுகிறது.',
        modRiskDesc: 'உங்களுக்கு மிதமான உடல்நல அபாயம் உள்ளது. ஆரோக்கியமான வாழ்க்கை முறை மாற்றங்களைச் செய்து உங்கள் உடல்நிலையைக் கண்காணிக்கவும்.',
        lowRiskDesc: 'உங்கள் உடல்நலக் குறிகாட்டிகள் ஆரோக்கியமான வரம்பிற்குள் உள்ளன. சமச்சீர் வாழ்க்கை முறையைத் தொடர்ந்து பராமரிக்கவும்.'
      }
    }
  }
};

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng: 'en',
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false
    }
  });

export default i18n;
