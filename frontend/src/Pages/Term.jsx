import React from 'react';

const TermsAndConditions = () => {
  return (
    <div className="container mx-auto p-8 bg-gradient-to-b from-green-100 to-green-200 text-gray-800">
      <div className="max-w-4xl mx-auto bg-white p-10 rounded-lg shadow-lg">
        <h1 className="text-4xl font-bold text-center mb-8">Terms and Conditions</h1>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-4">1. Introduction</h2>
          <p className="leading-relaxed">
            Welcome to Buy Hive. These terms and conditions outline the rules and regulations for the use of our website.
          </p>
        </div>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-4">2. Intellectual Property Rights</h2>
          <p className="leading-relaxed">
            Other than the content you own, under these Terms, Buy Hive and/or its licensors own all the intellectual property rights and materials contained in this website.
          </p>
        </div>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-4">3. Restrictions</h2>
          <p className="leading-relaxed">
            You are specifically restricted from all of the following:
          </p>
          <ul className="list-disc list-inside mt-2 ml-4">
            <li className="mt-1">Publishing any website material in any other media.</li>
            <li className="mt-1">Selling, sublicensing, and/or otherwise commercializing any website material.</li>
            <li className="mt-1">Using this website in any way that is or may be damaging to this website.</li>
            <li className="mt-1">Using this website in any way that impacts user access to this website.</li>
            <li className="mt-1">Engaging in any data mining, data harvesting, data extracting, or any other similar activity in relation to this website.</li>
          </ul>
        </div>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-4">4. Your Content</h2>
          <p className="leading-relaxed">
            In these Terms and Conditions, “Your Content” shall mean any audio, video, text, images, or other material you choose to display on this website. By displaying Your Content, you grant Buy Hive a non-exclusive, worldwide irrevocable, sub-licensable license to use, reproduce, adapt, publish, translate, and distribute it in any and all media.
          </p>
        </div>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-4">5. No Warranties</h2>
          <p className="leading-relaxed">
            This website is provided “as is,” with all faults, and Buy Hive expresses no representations or warranties, of any kind related to this website or the materials contained on this website.
          </p>
        </div>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-4">6. Limitation of Liability</h2>
          <p className="leading-relaxed">
            In no event shall Buy Hive, nor any of its officers, directors, and employees, be held liable for anything arising out of or in any way connected with your use of this website whether such liability is under contract. Buy Hive, including its officers, directors, and employees, shall not be held liable for any indirect, consequential, or special liability arising out of or in any way related to your use of this website.
          </p>
        </div>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-4">7. Indemnification</h2>
          <p className="leading-relaxed">
            You hereby indemnify to the fullest extent Buy Hive from and against any and all liabilities, costs, demands, causes of action, damages, and expenses arising in any way related to your breach of any of the provisions of these Terms.
          </p>
        </div>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-4">8. Severability</h2>
          <p className="leading-relaxed">
            If any provision of these Terms is found to be invalid under any applicable law, such provisions shall be deleted without affecting the remaining provisions herein.
          </p>
        </div>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-4">9. Variation of Terms</h2>
          <p className="leading-relaxed">
            Buy Hive is permitted to revise these Terms at any time as it sees fit, and by using this website you are expected to review these Terms on a regular basis.
          </p>
        </div>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-4">10. Assignment</h2>
          <p className="leading-relaxed">
            Buy Hive is allowed to assign, transfer, and subcontract its rights and/or obligations under these Terms without any notification. However, you are not allowed to assign, transfer, or subcontract any of your rights and/or obligations under these Terms.
          </p>
        </div>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-4">11. Entire Agreement</h2>
          <p className="leading-relaxed">
            These Terms constitute the entire agreement between Buy Hive and you in relation to your use of this website and supersede all prior agreements and understandings.
          </p>
        </div>

        <div>
          <h2 className="text-2xl font-semibold mb-4">12. Governing Law & Jurisdiction</h2>
          <p className="leading-relaxed">
            These Terms will be governed by and interpreted in accordance with the laws of the State of [Your State], and you submit to the non-exclusive jurisdiction of the state and federal courts located in [Your State] for the resolution of any disputes.
          </p>
        </div>
      </div>
    </div>
  );
}

export default TermsAndConditions;