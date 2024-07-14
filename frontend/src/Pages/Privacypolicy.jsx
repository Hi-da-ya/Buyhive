import React from 'react';

const PrivacyPolicy = () => {
  return (
    <div className="container mx-auto p-8 bg-gray-50 text-gray-800">
      <div className="max-w-4xl mx-auto bg-white p-10 rounded-lg shadow-lg">
        <h1 className="text-4xl font-bold text-center mb-8">Privacy Policy</h1>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-4">Introduction</h2>
          <p className="leading-relaxed">
            At Buy Hive, we are committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website.
          </p>
        </div>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-4">Information Collection</h2>
          <p className="leading-relaxed">
            We may collect information about you in a variety of ways. The information we may collect on the Site includes:
          </p>
          <ul className="list-disc list-inside mt-2 ml-4">
            <li className="mt-1">Personal Data: Personally identifiable information, such as your name, shipping address, email address, and telephone number.</li>
            <li className="mt-1">Derivative Data: Information our servers automatically collect when you access the Site, such as your IP address, browser type, and operating system.</li>
          </ul>
        </div>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-4">Use of Information</h2>
          <p className="leading-relaxed">
            Having accurate information about you permits us to provide you with a smooth, efficient, and customized experience. Specifically, we may use the information we collect to:
          </p>
          <ul className="list-disc list-inside mt-2 ml-4">
            <li className="mt-1">Create and manage your account.</li>
            <li className="mt-1">Process your transactions.</li>
            <li className="mt-1">Email you regarding your account or order.</li>
            <li className="mt-1">Improve our website and services.</li>
          </ul>
        </div>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-4">Disclosure of Information</h2>
          <p className="leading-relaxed">
            We may share information we have collected about you in certain situations. Your information may be disclosed as follows:
          </p>
          <ul className="list-disc list-inside mt-2 ml-4">
            <li className="mt-1">By Law or to Protect Rights: If we believe the release of information about you is necessary to respond to legal process, to investigate or remedy potential violations of our policies, or to protect the rights, property, and safety of others.</li>
            <li className="mt-1">Business Transfers: We may share or transfer your information in connection with, or during negotiations of, any merger, sale of company assets, financing, or acquisition of all or a portion of our business to another company.</li>
          </ul>
        </div>

        <div className="mb-6">
          <h2 className="text-2xl font-semibold mb-4">Security of Your Information</h2>
          <p className="leading-relaxed">
            We use administrative, technical, and physical security measures to help protect your personal information. While we have taken reasonable steps to secure the personal information you provide to us, please be aware that despite our efforts, no security measures are perfect or impenetrable, and no method of data transmission can be guaranteed against any interception or other type of misuse.
          </p>
        </div>

        <div>
          <h2 className="text-2xl font-semibold mb-4">Contact Us</h2>
          <p className="leading-relaxed">
            If you have questions or comments about this Privacy Policy, please contact us at:
          </p>
          <p className="mt-2">Email: support@buyhive.com</p>
          <p>Phone: (123) 456-7890</p>
        </div>
      </div>
    </div>
  );
}

export default PrivacyPolicy;