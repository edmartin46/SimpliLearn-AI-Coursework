function getPriorityFromString(subject) {
  let priority = "Low"; 
  if (/(urgent|critical|immediately|down)/i.test(subject)) priority = "High"; 
  else if (/(issue|problem|error|delay)/i.test(subject))   priority = "Medium"; 
  return priority;
}

const items = $input.all();
const emailData = items.map((item) => ({
  timestamp: new Date().toISOString(),
  subject: item?.json?.Subject,
  sender: item?.json?.From,
  body: item?.json?.snippet,
  priority: getPriorityFromString(item?.json?.Subject)
}));
return emailData;
