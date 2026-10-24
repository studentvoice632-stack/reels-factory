 left

0/1000 Executions
 
MASTER PROMPT: BUILD A FULLY AUTOMATED AI REELS & YOUTUBE SHORTS FACTORY

1. YOUR ROLE

Act as a senior automation architect, AI workflow engineer, video editing developer, API integration specialist, and quality assurance engineer.

Your task is to design and implement a complete, beginner-friendly, end-to-end automated content creation system using n8n or another suitable automation platform.

Do not merely explain the concept. Help me build the actual working system step by step, with importable workflows, code, configuration instructions, API setup guidance, and testing procedures.

Prioritize reliability, accurate information, cinematic video quality, ease of use, zero-cost operation, and automated publishing.

2. MY REQUIREMENTS AND CONSTRAINTS

- I have an Android mobile phone.
- I do not have a dedicated computer or laptop.
- My budget is ₹0.
- I prefer tools with genuinely usable free tiers.
- A free trial of 7–14 days is acceptable for testing, but the final solution must not depend on a paid subscription.
- I am a beginner and need simple, detailed instructions.
- I want the automation to work without my manually editing every video.
- The system should eventually operate on a daily schedule.
- My primary output platforms are YouTube Shorts and Instagram Reels.
- I want a WhatsApp message to trigger a workflow and receive the final report.
- Publishing should be automatic after the system passes its quality checks.
- Never claim that a tool, integration, or feature works unless it has been verified.

If a completely free, always-on solution is technically impossible with the available services, explain the exact limitation and propose the closest practical zero-cost alternative. Never silently introduce paid dependencies.

3. INPUT SYSTEM

Create a simple WhatsApp-based input interface.

I should be able to send messages such as:

- "Create today's trending cinematic reel."
- "Topic: mysterious facts about space."
- "Create a motivational reel with cinematic typography."
- "Research a trending song and build a suitable reel concept."
- "Create a 35-second YouTube Short about an interesting science fact."

The system must interpret the message, identify the requested topic, content category, language, duration, and publishing destinations, and then start the correct workflow.

If I provide only a topic, automatically choose suitable creative details without asking unnecessary questions.

If I provide no topic, research suitable current trends using permitted sources.

Support Hindi, Hinglish, and English where practical.

4. TREND RESEARCH AND FACT-CHECKING

Build a research stage that:

1. Searches permitted, accessible sources for current topics and trends.
2. Identifies promising topics based on relevance, recency, audience interest, and suitability for short-form video.
3. Uses available official sources, public trend data, search results, and platform-supported APIs where possible.
4. Records the source URLs and retrieval dates.
5. Verifies factual claims against reliable sources whenever feasible.
6. Avoids presenting speculation, rumours, or AI-generated assumptions as facts.
7. Does not invent trending statistics, song rankings, lyrics, source URLs, or popularity figures.
8. Distinguishes verified facts from creative interpretation.
9. Selects one suitable topic and explains internally why it was chosen.
10. Continues automatically if a source is unavailable, while recording the limitation.

For music trends, use only sources whose terms permit the intended access. Spotify popularity data must not automatically be treated as a definitive Instagram or YouTube trend ranking.

Do not scrape private data, bypass access restrictions, or violate platform terms.

5. MUSIC AND COPYRIGHT SAFETY

If a song-based reel is requested:

1. Research whether the song is relevant to the chosen concept.
2. Do not assume that publicly available lyrics or audio are free to reuse.
3. Do not reproduce complete copyrighted lyrics or obtain audio through unauthorized downloads.
4. Prefer properly licensed music, original generated audio, or tracks from legitimate royalty-free libraries.
5. Verify the applicable licence, attribution requirements, and commercial-use restrictions.
6. Where a trending commercial song requires in-platform licensing, prepare a compatible video and report that the song must be added through the platform's authorized music feature.
7. Never falsely report that a song is copyright-safe without adequate evidence.

If suitable licensed audio cannot be verified, use an alternative permitted track rather than stopping the entire workflow.

6. AI SCRIPT AND CREATIVE DIRECTION

Generate a complete, original, engaging short-form video concept.

The script should include:

- A strong opening hook.
- A clear central idea or story.
- A logical progression.
- Appropriate emotional or visual development.
- A satisfying ending.
- A natural call to action when appropriate.

Target duration: 30–45 seconds unless the input specifies otherwise.

Prepare a scene-by-scene production plan. For each scene, specify:

- Scene number.
- Start and end time.
- Narration or dialogue.
- Visual description.
- Text displayed on screen.
- Typography and text animation.
- Camera movement or simulated movement.
- Transition.
- Sound effects or music cues.
- Required visual assets.
- Source or generation method.

Make the narration duration match the video duration. Avoid unnecessary words, repetitive dialogue, generic filler, and misleading hooks.

For factual videos, preserve factual accuracy even when a more sensational claim would attract attention.

7. CINEMATIC VIDEO DESIGN AND TYPOGRAPHY

Produce professional-looking vertical videos in a 9:16 aspect ratio, preferably 1080 × 1920 when the rendering environment supports it.

The visual style should be cinematic, modern, polished, and appropriate to the selected song or story.

Include where suitable:

- Carefully timed typography.
- Dynamic but readable text animation.
- Smooth transitions.
- Appropriate visual pacing.
- Consistent font hierarchy.
- Balanced contrast.
- Safe margins for platform interfaces.
- Proper audio levels.
- Subtle motion and visual effects.
- Consistent colour grading.
- Accurate subtitle timing.
- Clean opening and ending frames.

Typography must match the mood and timing of the narration or music.

Use readable fonts with appropriate licences. Support Devanagari correctly for Hindi text.

Do not use arbitrary symbols, broken characters, random line breaks, misspelled words, or text that is cropped by the frame.

Do not imitate a particular living artist's exact style. Use general creative descriptions such as cinematic, minimalist, dramatic, documentary, or futuristic.

8. VIDEO PRODUCTION ENGINE

Use FFmpeg or another verified free and suitable video-rendering engine.

The workflow should:

1. Retrieve approved visual assets or generate them through a genuinely accessible service.
2. Generate or obtain narration where required.
3. Prepare subtitles and typography.
4. Combine visuals, narration, permitted music, and effects.
5. Render the final MP4.
6. Save the output in an accessible location.
7. Return a usable video URL or file reference to subsequent workflow steps.
8. Handle missing assets, invalid files, rendering failures, and timeouts.
9. Retry transient errors within reasonable limits.
10. Avoid creating duplicate outputs during retries.

Use appropriate video and audio codecs supported by the target platforms. Validate the resulting file rather than assuming a successful render means a playable video.

Do not assume FFmpeg can execute directly inside a cloud automation service. Verify whether the selected environment supports it, and provide an alternative if it does not.

9. THUMBNAIL, TITLE, DESCRIPTION, AND METADATA

For each video, generate platform-appropriate metadata.

YouTube Shorts

- Accurate, engaging title.
- Concise description.
- Relevant search keywords.
- Appropriate hashtags.
- Thumbnail image where supported and useful.
- Correct language and audience settings.
- Appropriate visibility settings.
- Source or attribution details when required.

Instagram Reels

- Engaging caption.
- Relevant hashtags.
- Appropriate account and audience settings.
- Cover image where supported.
- Suitable alt text or accessibility information where available.

Do not keyword-stuff, invent claims, misrepresent the video, or promise virality.

Ensure all text complies with the relevant platform's current limits.

10. AUTOMATIC PUBLISHING

Integrate official, permitted publishing interfaces.

YouTube

Use the YouTube Data API and OAuth authorization where required.

Upload the final video with its metadata. Check the returned video identifier and publication status.

Account for API quotas, processing delays, upload errors, and any restrictions affecting unverified API projects.

Instagram

Use the official Instagram publishing API or another currently supported official publishing integration.

Verify the account type, permissions, publishing eligibility, media URL requirements, and applicable API restrictions.

Handle the media-container creation, processing status, publishing operation, and returned media identifier where required by the API.

Do not assume that every Instagram account or every media format supports automated publishing.

General rules

- Publish only after all mandatory quality checks pass.
- Do not upload the same video repeatedly because of an ambiguous API response.
- Store publication identifiers to support duplicate prevention.
- Record the actual returned status.
- Do not claim a video was published if the API only accepted it for processing.
- If one platform succeeds and another fails, preserve the successful result and report the failure separately.
- Respect platform policies and account restrictions.

11. AUTOMATIC QUALITY ASSURANCE

Before publishing, run automated checks for:

- File existence and readability.
- Correct aspect ratio and resolution.
- Valid video duration.
- Valid audio stream.
- Audio/video synchronisation.
- Black or blank frames where detectable.
- Missing or corrupt visual assets.
- Subtitle timing.
- Text clipping and safe margins where technically detectable.
- Empty titles or descriptions.
- Broken metadata.
- Duplicate publication attempts.
- Copyright or licensing concerns identified by the workflow.
- Unsupported formats and file-size restrictions.

Use programmatic checks wherever possible. Use visual inspection or a suitable image/video analysis model where available.

Never claim to detect every possible typo or visual defect automatically. Identify which checks are deterministic and which are approximate.

If a critical check fails, do not publish the video. Retry, regenerate the affected asset, or mark the task as failed.

12. WHATSAPP INPUT AND FINAL REPORT

Use a supported WhatsApp integration with proper authentication and permissions.

After the workflow finishes, send a concise report containing:

- Requested topic.
- Selected concept.
- Video duration.
- Research status.
- Rendering status.
- YouTube upload status and link.
- Instagram publishing status and link.
- Thumbnail or preview link where available.
- Any skipped steps.
- Any errors and their reasons.
- Any required manual action.
- Actual usage or quota limitations encountered.

Example:

"Content Factory Report

Topic: Space Mystery
Research: Completed
Script: Completed
Video rendering: Completed
Quality checks: Passed

YouTube: Published
Link: [actual returned link]

Instagram: Published
Link: [actual returned link]

Music: Licensed alternative used
Errors: None

Task status: Completed"

Populate all fields from actual workflow results. Never invent links or report success before receiving confirmation.

If the workflow fails, send a failure report rather than remaining silent.

13. AUTOMATION SCHEDULING

Support both:

- Manual execution triggered by WhatsApp.
- Scheduled daily execution at a configurable time.

The daily workflow should research a suitable topic, generate the content, validate it, publish it, and send a WhatsApp report.

Avoid duplicate daily posts by storing a unique job identifier and publication records.

Make the workflow safe to restart after interruptions.

14. ZERO-COST INFRASTRUCTURE

Investigate the actual current free limits of every proposed service.

For each service, document:

- What the free tier includes.
- Whether a payment method is required.
- API quotas and rate limits.
- Daily or monthly usage limits.
- Storage and file-size restrictions.
- Whether workflows sleep or stop when idle.
- Whether FFmpeg can execute there.
- Whether outbound HTTP requests are supported.
- Whether OAuth credentials and persistent storage are supported.
- Whether scheduled workflows continue running reliably.
- Whether the service allows the intended commercial or public publishing use.
- What happens when the free limit is reached.

Prefer services with transparent free tiers and no mandatory paid dependency.

Do not use a free trial as evidence that a permanent free deployment is possible.

If no single platform can run the complete system for ₹0, split it into practical components and clearly explain the limitations.

Do not expose API keys, passwords, OAuth tokens, or WhatsApp credentials in workflow logs, public files, or source code.

15. IMPLEMENTATION PLAN

Build the system in the following order:

Phase 1: Validate the architecture and identify real free-tier limitations.

Phase 2: Create the workflow trigger and receive a test input.

Phase 3: Connect the AI service and generate a script.

Phase 4: Create a test video using FFmpeg or a verified rendering service.

Phase 5: Run automated quality checks and generate metadata.

Phase 6: Set up YouTube OAuth and publish a private or unlisted test video where appropriate.

Phase 7: Configure Instagram's official publishing integration and test it safely.

Phase 8: Configure WhatsApp input and final reporting.

Phase 9: Add scheduling, retries, error handling, logging, and duplicate prevention.

Phase 10: Run an end-to-end test and document how to operate the system from Android.

At each phase, give me the exact next actions and explain where to tap, what to paste, what to configure, and how to confirm success.

Do not ask me to complete many unrelated setup tasks at once. Give me a small set of actionable steps, wait for the required information or confirmation, and then continue.

16. REQUIRED DELIVERABLES

Provide:

1. A verified architecture diagram.
2. A tool-by-tool compatibility and free-tier table.
3. A list of required accounts and credentials.
4. A clear workflow map with nodes and their connections.
5. Importable n8n workflow JSON where applicable.
6. Required FFmpeg commands and supporting code.
7. API configuration instructions.
8. Secure credential-handling instructions.
9. Error-handling and duplicate-prevention logic.
10. An end-to-end testing checklist.
11. A troubleshooting guide.
12. A realistic assessment of ongoing ₹0 operation.
13. A final operating guide suitable for an Android-only beginner.

Any generated workflow JSON must be syntactically valid and must not contain invented node types, fake credentials, fabricated endpoints, or unsupported operations. Validate the workflow against the actual platform version where possible.

If a feature cannot be completed without a paid service, state that clearly and provide the best free alternative.

17. FINAL SUCCESS CRITERIA

The system is considered operational only when it can:

1. Receive a valid input or scheduled trigger.
2. Research a suitable topic.
3. Generate a coherent script and production plan.
4. Render a playable vertical video.
5. Validate the video and metadata.
6. Publish successfully to each configured platform through permitted interfaces.
7. Prevent accidental duplicate uploads.
8. Send a WhatsApp report containing actual results and links.
9. Recover gracefully from failures.
10. Operate within the confirmed free-tier limits.

Start by evaluating the architecture and current free-tier limitations. Then recommend the simplest reliable implementation for an Android-only beginner with a ₹0 ongoing budget.

Do not simply give me a theoretical plan. Help me implement and test the system in manageable stages, and never claim that any step is completed until it has actually been verified.

Thought for 5m 10s
WhatsApp reports for the daily scheduled run can cost about ₹0.15 per message. How should those reports reach you?
Telegram for everything (simplest and free)
Which of these accounts do you already have?
Google account with a YouTube channel, Instagram Professional (Business/Creator) account linked to a Facebook Page

Thought for 1m 42s
I've built the first workflow, "Reels Factory - Phase 2-3 (Request to Script)" (ID ixm8PaShhFQsXb3A). It hasn't run for real yet: in the test, your message, the AI reply and the Telegram send were all simulated with sample data.

What it does:

Your Telegram bot receives your message, in English, Hindi or Hinglish.
Gemini, with Google Search turned on, works out the topic, category, language, length (35 seconds by default) and where to post. If you don't give a topic, it searches for a current one. It then writes a scene-by-scene script with sources, music guidance, and YouTube and Instagram titles and captions.
A checker rejects plans that are broken, have timing gaps, or have an empty or too-long title or caption. It also warns if the narration seems too fast or too slow for the length.
The bot replies with a report. If something fails, you get a failure message instead.
Test result: with the sample data, steps 1–4 ran without errors. The failure message for when the AI doesn't respond was never triggered, so it's untested.

Three limits:

The AI runs on n8n's Gateway credits. That means no API key is needed during the trial, but it isn't free forever. When we move to GitHub Actions, you'll need your own free Google AI Studio key.
Source links come from the AI's own search. I've told it never to invent links, but you should still spot-check them. The report says this too.
No video is made yet. That's Phase 4, which uses GitHub Actions.
Your next steps, all on your phone:

In Telegram, open @BotFather, send /newbot, and pick a name and a username ending in bot. BotFather replies with a token. Don't paste it here.
Open @userinfobot, send any message, and copy your numeric Id.
In the setup panel in this chat:
Connect Telegram by creating a credential and pasting the token there.
Paste your Id into the User IDs field (under Additional Fields). This makes the bot respond only to you.
Tell me when that's done. I'll then run one live test with a message like "Topic: mysterious facts about space" and check the real reply.

Before Phase 4, please also:

Create a free account at github.com and confirm your email.
Create a free account at pexels.com/api for stock video clips.
Telegram connect ho gya hai

Finished thinking
Badhiya, Telegram connect ho gaya. Live test se pehle ek cheez baaki hai:

Setup panel mein "User IDs" field abhi khaali hai. Iske bina bot kisi ka bhi message le lega, aur main test reply aapke chat par bhej nahi paunga.

Telegram mein @userinfobot kholiye aur koi bhi message bhejiye.
Woh aapko ek number dega, jaise Id: 123456789. Sirf yeh number copy kijiye.
Setup panel mein Telegram Request → User IDs field mein yeh number paste karke save kijiye.
Yeh number secret nahi hai, ise yahan chat mein bhi likh sakte hain.

Uske baad mujhe "done" likhiye. Main ek live test chalaunga, jaise "Topic: mysterious facts about space". Phir check karunga ki aapke bot par asli report aayi ya nahi. Pichla test sirf sample data par chala tha, isliye abhi tak kuch bhi asli mein test nahi hua hai.

Vo field kaise kholi user id

Finished thinking
Is field ko phone par dhoondhna mushkil ho sakta hai. Aapko use kholne ki zaroorat nahi hai, main khud bhar dunga:

Telegram mein @userinfobot kholiye aur /start bhejiye.
Woh reply mein Id: 123456789 jaisa ek number dega.
Sirf woh number yahan chat mein bhej dijiye.
Yeh number password ya token nahi hai, isliye chat mein bhejna safe hai. Bot token kabhi chat mein mat bhejiyega.

Number milte hi main use workflow mein daal dunga, taaki bot sirf aapke messages ka jawab de. Workflow badalne se pehle ek approval card aayega, usse approve karna hoga. Uske baad live test chalaunga aur check karunga ki report aapke bot par aayi ya nahi.

8647534087

Thought for 29s
ID save ho gayi hai. Ab live test chala raha hoon: Gemini sach mein ek script likhega aur aapke Telegram bot par report bhejega. Approval card aayega, approve karne par hi test chalega.


Thought for 1m 11s
User ID save ho gayi, aur live test mein asli result mila. Lekin report aapke Telegram tak nahi pahunchi.

Kya kaam kiya (asli run, sample data nahi):

Gemini ne Google Search ke saath "mysterious facts about space" par 35 second ki script banayi. Usmein 5 scenes the: dark matter, Fast Radio Bursts, aur Great Attractor. Har fact ke saath source link bhi tha.
Checker ne plan pass kiya, title aur caption bhi bane.
Kya fail hua:

Telegram ne message bhejte waqt "chat not found" error diya.
Telegram bots tab tak kisi ko message nahi bhej sakte jab tak woh vyakti pehle bot ko /start na bheje. Lagta hai aapne abhi tak apne naye bot ko message nahi kiya hai.
Script mein 3 kamiyan dikhi, maine prompt badal diya hai:

Narration bahut lambi thi: 35 second mein 132 shabd, yaani 3.8 shabd/second, jo bolne ke liye bahut tez hai. Ab 35 second ke liye zyada se zyada 84 shabd ki limit hai.
Ek source YouTube video tha: ab sirf NASA, universities, journals aur badi news sites jaise bharosemand sources lene ko kaha hai.
Title clickbait tha: "UNBELIEVABLE… SHOCK You!". Ab aise shabd aur capital letters band kar diye hain.
Yeh badlav save ho gaye hain, lekin abhi tak test nahi hue.

Aapka agla kadam:

Telegram mein apna bot kholiye. Uska username @BotFather ke message mein mila tha.
Neeche Start button dabaiye, ya /start bhejiye. Bot abhi jawab nahi dega, yeh normal hai.
Mujhe yahan "start kar diya" likhiye.
Uske baad main naye prompt ke saath dobara live test chalaunga. Phir check karunga ki report aapke Telegram par pahunchi aur script ki teeno kamiyan theek hui ya nahi.

Maine board father ko slash start message kar diya

Finished thinking
Thoda sa confusion hai: BotFather ko /start bhejne se kaam nahi banega. BotFather sirf naye bots banane ke liye hai. Error "chat not found" isliye aa raha hai kyunki aapke apne bot ne aapse abhi tak baat nahi ki hai. Telegram mein koi bot tabhi aapko message bhej sakta hai jab aap pehle us bot ko message karein.

Ye 4 steps karein (sirf phone se):

Telegram mein BotFather wali chat kholiye aur upar scroll karke wo message dhoondhiye jo bot banate time aaya tha ("Done! Congratulations on your new bot..."). Usme ek link hoga, jaise t.me/AapkeBotKaNaam_bot.
Agar wo message nahi mil raha, to BotFather ko /mybots bhejiye. Wo aapke bot ka naam (@username) dikha dega.
Us link par tap kijiye. Isse aapka apna bot khulega, BotFather nahi.
Neeche START button dabaiye, ya /start type karke bhejiye.
Bot shayad abhi koi reply nahi karega. Ye normal hai, kyunki workflow abhi publish nahi hua hai. Bas message chala jaana chahiye.
Ye ho jaaye to mujhe likhiye "apne bot ko start kar diya". Fir main live test dobara chalaunga aur check karunga ki:

report aapke Telegram par pahunchti hai ya nahi, aur
script ke naye rules kaam kar rahe hain ya nahi: chhoti narration, koi YouTube source nahi, aur clickbait title nahi.
Ho gya

Thought for 41s
Live test pass ho gaya (execution #3). Report aapke bot @EditoAura_Auto_Bot se Telegram par pahunch gayi (message id 3). Pura flow chala: Telegram request → Gemini research aur script → validation → report bhejna.

Naye script rules ka result:

Check	Result
Narration ki length	77 words (35s ke liye limit 84). Koi warning nahi
YouTube/social source	Koi nahi aaya
Title	"3 Unexplained Space Mysteries That Will Baffle You | #Shorts" (60 characters, ALL-CAPS nahi)
Scenes	6 scenes, 0 se 35 second tak, gaps nahi
Hashtags	10
2 kamiyan abhi bhi hain:

Report adhoori aa rahi hai. Gemini ke source links bahut lambe Google redirect links hain (vertexaisearch...). Inki wajah se Telegram par report "..." par kat jaati hai, aur aapko scenes aur title dikhte hi nahi. In links se ye bhi pata nahi chalta ki asli website kaunsi hai.
Title thoda clickbait hai. "That Will Baffle You" pichle wale se behtar hai, lekin perfect nahi.
Aur ek baat: AI fail hone par jo report aani chahiye ("Build AI Failure Report"), wo raasta abhi tak kabhi test nahi hua hai.

Mera suggestion: report ko chhota aur saaf karna:

lambe links hata kar sirf website ka naam dikhana (jaise nasa.gov),
title, scenes aur caption ko upar rakhna,
title ke liye "will shock / baffle you" jaise phrases ban karna.
Iske baad Phase 4 (GitHub Actions par video rendering) shuru karenge.

Aap bataiye:

"fix karo" likhein to main report wala fix karke dobara test karunga.
Saath mein ye bhi bataiye: kya aapne GitHub aur Pexels API accounts bana liye? Phase 4 ke liye dono chahiye.
Aage ka kam start kro

Thought for 1m 25s
Report ka naya format save ho gaya hai aur test mein sahi bana. Lekin is test se ek badi kami saamne aayi: Gemini script ke rules hamesha nahi maanta.

Kya badla (draft save ho gaya, test execution #4):

Lambe Google links hat gaye. Ab har fact ke saath website ka naam aata hai (jaise NOAA, Britannica).
Title, scenes, Instagram caption aur hashtags ab report mein upar aate hain, isliye "..." par cut nahi honge.
Agar title mein clickbait shabd ho to report mein Warning aata hai.
Test mein kya mila (topic: ocean facts, 30s):

Narration 119 words ki thi, jabki limit 72 hai. Ye 4 words/sec hai, jo bolne ke liye bahut tez hai.
Title tha "Mind-Blowing Ocean Facts You Won't Believe!", yaani clickbait. Mana kiya tha, phir bhi aaya. Achhi baat ye hai ki naye check ne ise pakad liya.
Ek fact ke sources mein YouTube aur Quora bhi the.
Test ki limits: is baar Telegram trigger aur report bhejna simulate kiye gaye the. Asli Telegram delivery pichle live test (#3) mein kaam kar chuki hai. AI fail hone wala raasta abhi bhi test nahi hua hai.

Matlab: sirf prompt mein rules likhne se kaam nahi chalega. Agar ye script seedha video mein gayi to voice bahut tez hogi aur title clickbait hoga.

Mera suggestion: ek automatic "Editor" step jodna. Agar script mein words zyada hon, title clickbait ho, ya YouTube/Quora source ho, to Gemini se automatic dubara likhwaya jaayega (max 2 baar). Agar fir bhi theek na ho, to report mein saaf likha aayega "QA failed" aur video aage nahi badhegi. Iske liye koi naya account nahi chahiye, ye bhi Gateway credits par chalega.

Iske baad Phase 4 (video banana) ke liye aapko 2 cheezein khud banani hongi, sirf phone se:

GitHub account (github.com) par sign up. Free hai.
Pexels API key (pexels.com/api) par account banakar "Get API key". Free hai.
Ye key kabhi bhi chat mein paste mat kijiye. Baad mein main bataunga ki ise kahan daalna hai.

Aap jawab dijiye:

"editor jodo" likhein to main ye step bana kar test karunga.
Aur bataiye ki GitHub aur Pexels accounts ban gaye ya nahi.
Aage kya kru jo bhi do samne.

Thought for 3m 21s
Automatic Editor step ab kaam kar raha hai, aur test se iska saboot mila hai.

Kya mila:

Live run (#6): Editor chala aur report aapke Telegram par pahunchi. Narration 53 words (limit 72), title "Amazing Ocean Facts: Depths, Oxygen, and Unexplored Wonders #Shorts" tha. Lekin Instagram caption mein "mind-blowing" reh gaya tha, aur report mein QA line nahi aayi.
Iske baad maine 2 fix kiye: caption mein bhi clickbait check, aur report mein QA line.
Fix ke baad test (#7): Gemini aur Editor dono asli chale. Is run mein sirf Telegram trigger aur bhejna simulate hue, isliye ye report aapke phone par nahi gayi. Pehle script ne QA fail kiya, Editor ne 1 baar dobara likha, fir QA passed:
57 words (limit 72)
Title: "5 Fascinating Ocean Facts: Depths, Pressure, and Hidden Life #Shorts"
Caption mein clickbait nahi tha
Sources: USGS, NOAA, Royal Museums Greenwich
Editor wala Gemini bhi Gateway credits par chalta hai, isliye koi key nahi chahiye.
Abhi bhi test nahi hua:

AI fail hone wali report.
Wo case jab 2 baar likhwane ke baad bhi QA fail ho jaaye. Code mein us case mein report "QA: FAILED - do not render" bolegi, lekin abhi tak aisa run nahi hua.
Workflow abhi draft hai, publish nahi kiya hai.

Ab Phase 4: video banana. Ye kaam main aapke bina nahi kar sakta, kyunki account aapke naam par banana hoga. Abhi sirf ye 3 steps kijiye:

Step 1: GitHub account

Phone ke browser (Chrome) mein github.com/signup kholiye.
Email, password aur username daaliye. Username chhota rakhiye, jaise editoaura.
Email par aaya code daal kar verify kijiye.
Plan poocha jaaye to Free chuniye.
Step 2: Pexels API key (video clips ke liye, free hai)

pexels.com/api kholiye aur Get Started dabakar account banaiye.
Form mein reason likhiye: "Personal project for creating short videos".
Key screen par aa jaayegi. Ise kahin share mat kijiye, chat mein bhi nahi. Bas itna dhyan rakhiye ki ye kahan dikhti hai.
Step 3: Mujhe bataiye

Aapka GitHub username kya hai? Ye secret nahi hai.
Kya Pexels key mil gayi? Sirf "haan" likhiye, key mat bhejiye.
Ye ho jaaye, to main aapko phone se hi ek GitHub repository banane aur usme video-rendering ka setup daalne ke steps dunga.

Ho gya

Finished thinking
Badhiya. Ab GitHub par video render karne ke liye ek repo banana hai. Ye steps phone ke browser se ho jaayenge. GitHub app se kuch settings nahi milti, isliye Chrome use karein.

Step 1: Repo banayein

Chrome mein github.com kholein aur login karein.
Upar right corner mein apni profile photo par tap karein, phir "Your repositories" kholein, aur phir hare rang ke "New" button par tap karein.
Ye
You stopped this run
studentvoice632-stack

Finished thinking
Username mil gaya: studentvoice632-stack. Pichhla message beech mein kat gaya tha, isliye poore steps dobara de raha hoon.

Step 1: Repo banayein (Chrome mein)

Ye link kholein: github.com/new
Repository name mein likhein: reels-factory
Public select karein. Public repo par GitHub Actions free milta hai. Aapki keys (jaise Pexels key) public nahi hongi, wo alag se chhupi hui jagah par jaayengi.
"Add a README file" wala option ON karein.
Neeche "Create repository" dabayein.
Step 2: Pexels key ko safe jagah rakhein

Naye repo ke page par upar menu mein Settings par tap karein. Agar Settings nahi dikhe, to menu ko left side swipe karein ya "..." par tap karein.
Left menu mein ye kholein: Secrets and variables, phir Actions.
"New repository secret" par tap karein.
Name mein likhein: PEXELS_API_KEY
Secret box mein apni Pexels key paste karein, phir "Add secret" dabayein.
Key sirf GitHub ke us box mein daalni hai. Yahan chat mein kabhi paste mat kijiye.

Dono steps ho jaayein to bas likh dijiye "repo aur secret ho gaya". Agar kahin atak jaayein, to batayein ki screen par kya dikh raha hai. Uske baad hum video render karne wala code repo mein daalenge.

Step 2 nhi aaya samj

Finished thinking
Koi baat nahi, Step 2 ko aasaan tareeke se karte hain. Menu dhoondhne ki zaroorat nahi hai, ek seedha link hai.

Pehle check kar lein ki Step 1 ho gaya hai, yaani reels-factory naam ka repo ban chuka hai. Agar nahi bana, to pehle github.com/new se wo bana lijiye.

Step 2 (seedhe link se)

Chrome ke address bar mein ye poora link paste karke kholein:
github.com/studentvoice632-stack/reels-factory/settings/secrets/actions/new
Ek page khulega jisme do box honge:
Name box mein likhein: PEXELS_API_KEY
Secret box mein apni Pexels key paste karein.
Neeche hare rang ka "Add secret" button dabayein.
Pexels key kahan milegi:
pexels.com/api kholein, login karein, aur wahan "Your API Key" ke neeche lambi si key dikhegi. Use copy kar lijiye.

Agar link "404" ya "Page not found" dikhaye:
Iska matlab hai ki repo ka naam alag hai ya repo abhi bana nahi. Us case mein mujhe batayein ki screen par kya dikh raha hai.

Ho jaaye to likh dijiye "secret ho gaya". Key yahan chat mein paste mat kijiye.

Pexepexels key kha sey pau

Finished thinking
Pexels key free milti hai. Phone ke Chrome mein ye steps karein:

Step A: Pexels account banayein

pexels.com/join kholein.
Apna Google account choose karein, ya email aur password se sign up karein.
Agar Pexels confirmation email bheje, to Gmail mein jaakar us link par tap karein.
Step B: API key lein

pexels.com/api kholein.
"Your API Key" ya "Get Started" button par tap karein.
Ek chhota form khul sakta hai. Usme aisa kuch bhar dijiye:
Project ka naam / description: Personal YouTube Shorts automation using stock videos
Website: apne YouTube channel ka link daal dijiye. Agar website wala box zaroori na ho to khaali chhod dijiye.
Terms wale box par tick karein aur submit karein.
Ab ek lambi si key dikhegi (letters aur numbers mix). Uske paas wale copy button par tap karein, ya key par long-press karke copy kar lijiye.
Form ke button ke naam thode alag ho sakte hain. Agar kuch alag dikhe to mujhe batayein ki screen par kya likha hai.

Step C: Key GitHub mein daalein
Ye pichhle message wala Step 2 hi hai: github.com/studentvoice632-stack/reels-factory/settings/secrets/actions/new kholein. Name mein PEXELS_API_KEY likhein, Secret box mein key paste karein, phir "Add secret" dabayein.

Ek baat yaad rakhein: key ko yahan chat mein paste nahi karna hai, sirf GitHub ke Secret box mein.

Ho jaaye to likh dijiye "secret ho gaya".

New API key issuance is currently paused and cannot be requested.”

Thought for 11s
Pexels ne nayi keys dena abhi band kar rakha hai, isliye uski jagah Pixabay use karte hain. Ye bhi free stock videos deta hai. Maine Pixabay ke official docs check kiye hain. Wahan likha hai ki login karne ke baad API key docs page par hi dikh jaati hai, alag se form bharne ki zaroorat nahi hoti. Lekin ye maine khud try karke confirm nahi kiya hai, isliye aap check karke batayein.

Step A: Pixabay account banayein

Chrome mein pixabay.com kholein.
Join ya Sign up par tap karein. Google account se ya email se account bana lijiye.
Agar confirmation email aaye, to Gmail mein jaakar us link par tap karein.
Step B: Key copy karein

Login rehte hue ye link kholein: pixabay.com/api/docs/
Page ko neeche scroll karke "Search Images" wale hisse tak jaayein. Wahan Parameters table mein key (required) ke saamne aapki lambi key likhi hogi (letters aur numbers mix).
Us key par long-press karke copy kar lijiye.
Step C: Key GitHub mein daalein

Ye link kholein: github.com/studentvoice632-stack/reels-factory/settings/secrets/actions/new
Name box mein likhein: PIXABAY_API_KEY
Secret box mein Pixabay key paste karein, phir "Add secret" dabayein.
Dhyan rakhne wali baatein:

Pixabay ki ek request hai ki aap batayein videos kahan se liye. Isliye hum har video ki description mein "Stock footage: Pixabay" khud likh denge.
Agar key ki jagah "Please login to see your API key" likha aaye, to iska matlab hai ki aap login nahi hain. Pehle login karke page refresh kijiye.
Agar Pixabay par bhi likha aaye ki keys abhi nahi mil rahi, to mujhe exact message bata dijiye. Phir hum dusra option dekhenge.
Key yahan chat mein paste mat kijiye. Ho jaaye to likh dijiye "pixabay secret ho gaya".

Ho gya

Thought for 40s
Pixabay key GitHub mein save ho gayi. Ab repo mein video banane wala code daalna hai. Isme 2 files banengi, phir ek test video banega.

Pehle saaf bata doon: ye code maine yahan khud chala kar test nahi kiya hai. Pehli baar chalane par error aa sakta hai. Aisa hua to error message ke hisaab se main fix kar dunga. Awaaz ke liye edge-tts use ho raha hai. Ye Microsoft ki free awaaz hai jisme key nahi chahiye, lekin ye official service nahi hai, to kabhi band ho sakti hai. Hindi subtitles ke liye alag font baad mein lagayenge, abhi test English mein hai.

Step 1: Pehli file render.py

Chrome mein kholein: github.com/studentvoice632-stack/reels-factory/new/main
Upar "Name your file" box mein likhein: render.py
Neeche wale code ke upar copy button dabayein aur bade box mein paste karein. Spaces bilkul mat badliye, Python mein spaces zaroori hain.
"Commit changes..." dabayein, phir popup mein dobara "Commit changes" dabayein.
import os, json, asyncio, subprocess, textwrap
import requests, edge_tts

SAMPLE = {"voice": "en-US-GuyNeural", "scenes": [
    {"text": "The ocean covers more than seventy percent of our planet.", "query": "ocean waves"},
    {"text": "Yet more than eighty percent of it has never been explored.", "query": "deep sea"},
    {"text": "Its deepest point is nearly eleven kilometers down.", "query": "underwater"}]}

job = json.loads(os.environ.get("JOB_JSON") or "null") or SAMPLE
KEY = os.environ["PIXABAY_API_KEY"]
VOICE = job.get("voice", "en-US-GuyNeural")
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
os.makedirs("out", exist_ok=True)
os.makedirs("tmp", exist_ok=True)

def run(cmd):
    subprocess.run(cmd, check=True)

def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return float(r.stdout.strip())

def get_clip(query, i):
    r = requests.get("https://pixabay.com/api/videos/",
                     params={"key": KEY, "q": query, "per_page": 5, "safesearch": "true"}, timeout=30)
    r.raise_for_status()
    hits = r.json().get("hits", [])
    if not hits:
        raise SystemExit("No Pixabay video for: " + query)
    sizes = hits[0]["videos"]
    url = next(sizes[s]["url"] for s in ("medium", "large", "small", "tiny")
               if sizes.get(s, {}).get("url"))
    path = f"tmp/clip{i}.mp4"
    with requests.get(url, stream=True, timeout=120) as d:
        d.raise_for_status()
        with open(path, "wb") as f:
            for chunk in d.iter_content(1 << 20):
                f.write(chunk)
    return path, hits[0]["pageURL"]

credits = []
with open("tmp/list.txt", "w") as lst:
    for i, scene in enumerate(job["scenes"]):
        text = scene["text"]
        mp3 = f"tmp/voice{i}.mp3"
        asyncio.run(edge_tts.Communicate(text, VOICE).save(mp3))
        dur = duration(mp3) + 0.3
        clip, page = get_clip(scene["query"], i)
        credits.append(page)
        sub = f"tmp/sub{i}.txt"
        with open(sub, "w") as f:
            f.write("\n".join(textwrap.wrap(text, 24)))
        vf = ("scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,"
              f"drawtext=fontfile={FONT}:textfile={sub}:fontsize=64:fontcolor=white:"
              "borderw=5:bordercolor=black:line_spacing=12:x=(w-text_w)/2:y=h*0.68")
        run(["ffmpeg", "-y", "-stream_loop", "-1", "-i", clip, "-i", mp3, "-t", f"{dur:.2f}",
             "-vf", vf, "-af", "apad", "-map", "0:v:0", "-map", "1:a:0",
             "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-ar", "44100", "-ac", "2", f"tmp/scene{i}.mp4"])
        lst.write(f"file 'scene{i}.mp4'\n")

run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "tmp/list.txt", "-c", "copy", "out/final.mp4"])
with open("out/credits.txt", "w") as f:
    f.write("Stock footage: Pixabay\n" + "\n".join(credits) + "\n")
print("Done: out/final.mp4", duration("out/final.mp4"), "sec")
